const express = require("express");
const mysql = require("mysql");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "aishhil2125",
    database: "oasis"
});

db.connect(err => {
    if (err) {
        console.error("Database connection failed: " + err.stack);
        return;
    }
    console.log("Connected to database");
});

// Register Farmer
app.post("/regfar", (req, res) => {
    const { name, MobileNumber, Accno, IFSC, branch } = req.body;
    const query = "INSERT INTO register_farmer (name, mobno, accno, ifsc, branch) VALUES (?, ?, ?, ?, ?)";
    
    db.query(query, [name, MobileNumber, Accno, IFSC, branch], (err, result) => {
        if (err) {
            console.error("Error registering farmer: ", err);
            return res.status(500).json({ error: "Database error" });
        }
        const token_id = result.insertId;
        const createTableQuery = `CREATE TABLE token_${token_id} (date DATE NULL, amount_per_ltr DECIMAL(10, 2) NULL, quantity DECIMAL(10, 2) NULL, total_amount DECIMAL(10, 2) NULL);`;
        
        db.query(createTableQuery, (err) => {
            if (err) {
                console.error("Error creating table: ", err);
                return res.status(500).json({ error: "Table creation failed" });
            }
            res.json({ message: "Registration successful", token: token_id });
        });
    });
});

// Buy Milk
app.post("/submitbuymilk", (req, res) => {
    const { FID, Quantity, Amount } = req.body;
    const expense = Quantity * Amount;
    
    const query = `INSERT INTO token_${FID} (date, amount_per_ltr, quantity, total_amount) VALUES (CURDATE(), ?, ?, ?)`;
    
    db.query(query, [Amount, Quantity, expense], (err) => {
        if (err) {
            console.error("Error buying milk: ", err);
            return res.status(500).json({ error: "Database error" });
        }
        res.json({ message: "Successfully recorded" });
    });
});

// Pay Farmer
app.post("/submitpayfarmer", (req, res) => {
    const { farmertokenid, amount } = req.body;
    
    const checkQuery = "SELECT COUNT(*) AS count FROM register_farmer WHERE token_id = ?";
    db.query(checkQuery, [farmertokenid], (err, result) => {
        if (err || result[0].count === 0) {
            return res.status(400).json({ error: "Invalid token ID" });
        }
        
        const totalAmountQuery = `SELECT SUM(quantity * amount_per_ltr) AS total FROM token_${farmertokenid}`;
        db.query(totalAmountQuery, (err, totalRes) => {
            const totalAmount = totalRes[0].total || 0;
            
            const paidQuery = "SELECT SUM(amount_paid) AS paid FROM pay_farmer WHERE token_id = ?";
            db.query(paidQuery, [farmertokenid], (err, paidRes) => {
                const amountPaidSoFar = paidRes[0].paid || 0;
                const netAmount = totalAmount - amountPaidSoFar;
                const finalAmount = Math.min(amount, netAmount);
                
                const insertQuery = "INSERT INTO pay_farmer (token_id, amount_paid) VALUES (?, ?)";
                db.query(insertQuery, [farmertokenid, finalAmount], (err) => {
                    if (err) return res.status(500).json({ error: "Database error" });
                    res.json({ message: "Successfully Paid", amountPaid: finalAmount });
                });
            });
        });
    });
});

// Show Farmers
app.get("/api/data", (req, res) => {
    const query = "SELECT token_id, name, mobno, accno, ifsc, branch FROM register_farmer";
    db.query(query, (err, farmers) => {
        if (err) return res.status(500).json({ error: "Database error" });
        
        const farmerData = farmers.map(farmer => {
            return new Promise(resolve => {
                const totalAmountQuery = `SELECT SUM(quantity * amount_per_ltr) AS total FROM token_${farmer.token_id}`;
                db.query(totalAmountQuery, (err, totalRes) => {
                    const totalAmount = totalRes[0]?.total || 0;
                    
                    const paidQuery = "SELECT SUM(amount_paid) AS paid FROM pay_farmer WHERE token_id = ?";
                    db.query(paidQuery, [farmer.token_id], (err, paidRes) => {
                        const amountPaid = paidRes[0]?.paid || 0;
                        resolve({ ...farmer, net_amount: Math.max(0, totalAmount - amountPaid) });
                    });
                });
            });
        });
        
        Promise.all(farmerData).then(data => res.json(data));
    });
});

// Show Overhead
app.get("/showoverhead", (req, res) => {
    const query = "SELECT date, expense_name, expense_amt, status FROM overhead";
    db.query(query, (err, rows) => {
        if (err) return res.status(500).json({ error: "Database error" });
        res.json(rows);
    });
});

app.get("/logistics", (req, res) => {
    db.query("SELECT * FROM logistics", (err, results) => {
      if (err) return res.status(500).send(err);
      res.json(results);
    });
  });
  
  // Register Vendor
app.post("/vendor", (req, res) => {
    const { vendor_name, contact, email } = req.body;
    const sql = "INSERT INTO vendor (vendor_name, contact, email) VALUES (?, ?, ?)";
    db.query(sql, [vendor_name, contact, email], (err, result) => {
      if (err) return res.status(500).send(err);
      res.json({ message: "Vendor Registered", vendorId: result.insertId });
    });
  });
  
  // Update Product Price
app.post("/update_price", (req, res) => {
    const { vendor_id, product_id, price } = req.body;
    const sql = "INSERT INTO product_prices (vendor_id, product_id, price) VALUES (?, ?, ?)";
    db.query(sql, [vendor_id, product_id, price], (err, result) => {
      if (err) return res.status(500).send(err);
      res.json({ message: "Product Price Updated" });
    });
  });
  
  // Fetch Vendor Data
app.get("/vendors", (req, res) => {
    db.query("SELECT * FROM vendor", (err, results) => {
      if (err) return res.status(500).send(err);
      res.json(results);
    });
  });
  
  // Sell Product and Update Inventory
app.post("/sell_product", (req, res) => {
    const { product_id, quantity_sold } = req.body;
  
    db.beginTransaction((err) => {
      if (err) return res.status(500).send(err);
  
      // Check available stock
      db.query("SELECT stock FROM total WHERE product_id = ?", [product_id], (err, results) => {
        if (err) return db.rollback(() => res.status(500).send(err));
        if (results.length === 0 || results[0].stock < quantity_sold) {
          return db.rollback(() => res.status(400).json({ message: "Insufficient Stock" }));
        }
  
        // Update stock
        db.query("UPDATE total SET stock = stock - ? WHERE product_id = ?", [quantity_sold, product_id], (err) => {
          if (err) return db.rollback(() => res.status(500).send(err));
  
          db.commit((err) => {
            if (err) return db.rollback(() => res.status(500).send(err));
            res.json({ message: "Product Sold, Stock Updated" });
          });
        });
      });
    });
});

// Product Production
app.post("/productproduction", (req, res) => {
    const fields = ["MilkCM500", "MilkCM200", "MilkTM500", "MilkTM200", "Lassi200", "LassiCUP200", "LassiMANGOCUP200", "Dahi200", "Dahi500", "Dahi2LT", "Dahi5LT", "Dahi10LT", "Dahi2LT15", "Dahi5LT15", "Dahi10LT15", "Buttermilk", "Khova500", "Khoya1000", "Shrikhand100", "Shrikhand250", "Ghee200", "Ghee500", "Ghee15LT", "Paneerloose", "khovaloose"];
    const values = fields.map(field => req.body[field] || 0);
  
    const sql = `INSERT INTO total (id, ${fields.join(", ")}) VALUES (1, ${fields.map(() => "?").join(", ")}) 
                ON DUPLICATE KEY UPDATE ${fields.map(field => `${field} = ${field} + VALUES(${field})`).join(", ")}`;
  
    db.query(sql, values, (err, result) => {
      if (err) return res.status(500).send(err);
      res.json({ message: "Product quantities have been successfully recorded." });
    });
  });
  
  // Get Vendor Payment Info
app.post("/get_vendor", (req, res) => {
    const { vendorId } = req.body;
    db.query("SELECT amount FROM vendor WHERE token = ?", [vendorId], (err, result) => {
      if (err) return res.status(500).send(err);
      if (result.length === 0) return res.status(404).json({ error: "Vendor not found" });
      res.json({ amount: result[0].amount });
    });
  });
  
  // Update Vendor Payment
  app.post("/update_vendor", (req, res) => {
    const { vendorId, paidAmount } = req.body;
    db.query("SELECT amount FROM vendor WHERE token = ?", [vendorId], (err, result) => {
      if (err) return res.status(500).send(err);
      if (result.length === 0) return res.status(404).json({ error: "Vendor not found" });
  
      const newAmount = result[0].amount - paidAmount;
      db.query("UPDATE vendor SET amount = ? WHERE token = ?", [newAmount, vendorId], (err) => {
        if (err) return res.status(500).send(err);
        res.json({ new_amount: newAmount });
      });
    });
  }); 
  
  
  // Fetch Vendor Transaction Data
app.post("/VendorTransaction", (req, res) => {
    const { vendor_id } = req.body;
    if (!vendor_id) {
      return res.status(400).json({ error: "Vendor ID is required" });
    }
  
    const query = `SELECT * FROM ??`;
    db.query(query, [vendor_id], (err, results) => {
      if (err) return res.status(500).send(err);
      if (results.length === 0) return res.status(404).json({ error: "No data found" });
      res.json(results);
    });
  });
  
  // Submit Logistics Expense
  app.post("/submitlogistics", (req, res) => {
    const { title, expense, status } = req.body;
    const query = "INSERT INTO logistics (date, expense_name, status, expense_amt) VALUES (CURDATE(), ?, ?, ?)";
    db.query(query, [title, status, expense], (err, result) => {
      if (err) return res.status(500).send(err);
      res.json({ message: "Successfully recorded" });
    });
  });
  
  // Submit Overhead Expense
  app.post("/submitoverhead", (req, res) => {
    const { title, expense, status } = req.body;
    const query = "INSERT INTO overhead (date, expense_name, status, expense_amt) VALUES (CURDATE(), ?, ?, ?)";
    db.query(query, [title, status, expense], (err, result) => {
      if (err) return res.status(500).send(err);
      res.json({ message: "Successfully recorded" });
    });
  });
  
  // Manage Vehicles
  app.post("/manage", (req, res) => {
    const { truckNumber, driverName, source, destination, truckModel, kilometers } = req.body;
    const query = "INSERT INTO managetrucks (tkdate, truckNo, driverName, source, destination, truckModel, kilometers) VALUES (CURDATE(), ?, ?, ?, ?, ?, ?)";
    db.query(query, [truckNumber, driverName, source, destination, truckModel, kilometers], (err, result) => {
      if (err) return res.status(500).send(err);
      res.json({ message: "Vehicle Recorded Successfully" });
    });
  });
  
  // Fetch Truck Details
  app.get("/truckdetails", (req, res) => {
    db.query("SELECT * FROM managetrucks", (err, results) => {
      if (err) return res.status(500).send(err);
      res.json(results);
    });
  });


  app.post("/submitrawmaterial", (req, res) => {
    const inputFields = [
      "MilkCM500RolePrice", "MilkCM500RoleQuan",
      "MilkCM200RolePrice", "MilkCM200RoleQuan",
      "MilkTM500RolePrice", "MilkTM500RoleQuan",
      "MilkTM200RolePrice", "MilkTM200RoleQuan",
      "Lassi200RolePrice", "Lassi200RoleQuan",
      "LassiCUP200cupPrice", "LassiCUP200cupQuan",
      "LassiMANGOCUP200cupPrice", "LassiMANGOCUP200cupQuan",
      "Dahi200MLRolePrice", "Dahi200MLRoleQuan",
      "Dahi500MLRolePrice", "Dahi500MLRoleQuan",
      "Dahi2LTBucketPrice", "Dahi2LTBucketQuan",
      "Dahi5LTBucketPrice", "Dahi5LTBucketQuan",
      "Dahi10LTBucketPrice", "Dahi10LTBucketQuan",
      "Dahi2LT1_5BucketPrice", "Dahi2LT1_5BucketQuan",
      "Dahi5LT1_5BucketPrice", "Dahi5LT1_5BucketQuan",
      "Dahi10LT1_5BucketPrice", "Dahi10LT1_5BucketQuan",
      "ButtermilkRolePrice", "ButtermilkRoleQuan",
      "Khova500TinPrice", "Khova500TinQuan",
      "Khoya1000TinPrice", "Khoya1000TinQuan",
      "Shrikhand100TinPrice", "Shrikhand100TinQuan",
      "Shrikhand250TinPrice", "Shrikhand250TinQuan",
      "Ghee200TinPrice", "Ghee200TinQuan",
      "Ghee500TinPrice", "Ghee500TinQuan",
      "Ghee15LTTinPrice", "Ghee15LTTinQuan",
      "PaneerloosePrice", "PaneerlooseQuan",
      "khovaloosePrice", "khovalooseQuan",
      "LASSICUPFOILPrice", "LASSICUPFOILQuan",
      "IFFFLAVERMANGOPrice", "IFFFLAVERMANGOQuan",
      "IFFFLAVERVANILLAPrice", "IFFFLAVERVANILLAQuan",
      "CULTUREAMAZIKAPrice", "CULTUREAMAZIKAQuan",
      "CULTUREDANISKOPrice", "CULTUREDANISKOQuan",
      "CULTUREHRPrice", "CULTUREHRQuan",
      "LIQUIDSOAPPrice", "LIQUIDSOAPQuan",
      "COSSODAPrice", "COSSODAQuan",
      "KAOHPrice", "KAOHQuan",
    ];
  
    let data = {};
  
    inputFields.forEach((field) => {
      let value = req.body[field] || "0";
      data[field] = field.includes("Price") ? parseFloat(value) : parseInt(value, 10);
    });
  
    const query = `
      INSERT INTO raw_materials (
        buydate, ${inputFields.join(", ")}
      ) VALUES (
        CURDATE(), ${inputFields.map(() => "?").join(", ")}
      )
      ON DUPLICATE KEY UPDATE ${inputFields
        .map((field) => `${field} = ${field} + VALUES(${field})`)
        .join(", ")};
    `;
  
    db.query(query, Object.values(data), (err, result) => {
      if (err) {
        console.error("Error inserting/updating raw materials:", err);
        return res.status(500).send({ error: "Database error" });
      }
  
      // Update total quantities
      const totalQuery = `
        INSERT INTO total_quantities (
          id, ${inputFields.filter((f) => f.includes("Quan")).join(", ")}
        ) VALUES (
          1, ${inputFields.filter((f) => f.includes("Quan")).map(() => "?").join(", ")}
        )
        ON DUPLICATE KEY UPDATE ${inputFields
          .filter((f) => f.includes("Quan"))
          .map((field) => `${field} = ${field} + VALUES(${field})`)
          .join(", ")};
      `;
  
      db.query(
        totalQuery,
        inputFields.filter((f) => f.includes("Quan")).map((field) => data[field]),
        (err, result) => {
          if (err) {
            console.error("Error updating total quantities:", err);
            return res.status(500).send({ error: "Database error in total_quantities" });
          }
  
          res.send({ success: "Raw material submitted successfully" });
        }
      );
    });
  });

  
  app.post("/userawmaterial", async (req, res) => {
    const inputFields = [
      "MilkCM500RoleQuan", "MilkCM200RoleQuan", "MilkTM500RoleQuan", "MilkTM200RoleQuan",
      "Lassi200RoleQuan", "LassiCUP200cupQuan", "LassiMANGOCUP200cupQuan", "Dahi200MLRoleQuan",
      "Dahi500MLRoleQuan", "Dahi2LTBucketQuan", "Dahi5LTBucketQuan", "Dahi10LTBucketQuan",
      "Dahi2LT1_5BucketQuan", "Dahi5LT1_5BucketQuan", "Dahi10LT1_5BucketQuan", "ButtermilkRoleQuan",
      "Khova500TinQuan", "Khoya1000TinQuan", "Shrikhand100TinQuan", "Shrikhand250TinQuan",
      "Ghee200TinQuan", "Ghee500TinQuan", "Ghee15LTTinQuan", "PaneerlooseQuan",
      "khovalooseQuan", "LASSICUPFOILQuan", "IFFFLAVERMANGOQuan", "IFFFLAVERVANILLAQuan",
      "CULTUREAMAZIKAQuan", "CULTUREDANISKOQuan", "CULTUREHRQuan", "LIQUIDSOAPQuan",
      "COSSODAQuan", "KAOHQuan"
    ];
  
    try {
      const data = {};
      inputFields.forEach(field => {
        data[field] = parseInt(req.body[field] || "0", 10);
      });
  
      // Construct the update query
      const updateQuery = `
        UPDATE total_quantities
        SET ${inputFields.map(field => `${field} = ${field} - ?`).join(", ")}
        WHERE id = 1;
      `;
  
      // Execute the update query
      const [result] = await db.execute(updateQuery, inputFields.map(field => data[field]));
  
      res.status(200).json({
        message: "Successfully updated raw materials",
        affectedRows: result.affectedRows
      });
  
    } catch (error) {
      console.error("Error updating raw materials:", error);
      res.status(500).json({
        message: "An error occurred while updating raw materials",
        error: error.message
      });
    }
  });
  
  // GET: Fetch Raw Materials
  app.get("/get-raw-materials", async (req, res) => {
    try {
      const query = `
        SELECT * FROM total_quantities WHERE id = 1;
      `;
  
      const [rows] = await db.execute(query);
  
      if (rows.length === 0) {
        return res.status(404).json({ message: "No raw materials found." });
      }
  
      res.json(rows[0]);
  
    } catch (error) {
      console.error("Error fetching raw materials:", error);
      res.status(500).json({
        message: "An error occurred while fetching raw materials",
        error: error.message
      });
    }
  });
  

app.listen(5000, () => {
    console.log("Server running on port 5000");
});

