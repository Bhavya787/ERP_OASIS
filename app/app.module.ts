import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
// import { HttpClient } from '@angular/common/http';
// import { FormsModule } from '@angular/forms';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterFarmerComponent } from './register-farmer/register-farmer.component';
import { BuyMilkComponent } from './buy-milk/buy-milk.component';
import { PayFarmerComponent } from './pay-farmer/pay-farmer.component';
import { MilkBifurcationComponent } from './milk-bifurcation/milk-bifurcation.component';
import { RegisterVendorComponent } from './register-vendor/register-vendor.component';
import { SellProductsComponent } from './sell-products/sell-products.component';
import { VendorStatusComponent } from './vendor-status/vendor-status.component';
import { ManageTrucksComponent } from './manage-trucks/manage-trucks.component';
import { OverheadComponent } from './overhead/overhead.component';
import { LogisticsComponent } from './logistics/logistics.component';
import { RawMaterialsComponent } from './raw-materials/raw-materials.component';
import { ShowFarmersComponent } from './show-farmers/show-farmers.component';
import { ShowVendorsComponent } from './show-vendors/show-vendors.component';
import { ProductPricesComponent } from './product-prices/product-prices.component';
import { TruckDetailsComponent } from './truck-details/truck-details.component';
import { OverHeadDetailsComponent } from './over-head-details/over-head-details.component';
import { LogisticsDetailsComponent } from './logistics-details/logistics-details.component';
import { RawMaterialsDeatailsComponent } from './raw-materials-deatails/raw-materials-deatails.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { UseRawMaterialComponent } from './use-raw-material/use-raw-material.component';
import { VendorPaymentsComponent } from './vendor-payments/vendor-payments.component';
import { VendorService } from './vendor.service';
import { ProductProductionComponent } from './product-production/product-production.component';
// import { VendorTransactionsComponent } from './vendor-transactions/vendor-transactions.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterFarmerComponent,
    BuyMilkComponent,
    PayFarmerComponent,
    MilkBifurcationComponent,
    RegisterVendorComponent,
    SellProductsComponent,
    VendorStatusComponent,
    ManageTrucksComponent,
    OverheadComponent,
    LogisticsComponent,
    RawMaterialsComponent,
    ShowFarmersComponent,
    ShowVendorsComponent,
    ProductPricesComponent,
    TruckDetailsComponent,
    OverHeadDetailsComponent,
    LogisticsDetailsComponent,
    RawMaterialsDeatailsComponent,
    UseRawMaterialComponent,
    VendorPaymentsComponent,
    ProductProductionComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FontAwesomeModule,
    HttpClientModule,
    CommonModule
  ],
  providers: [VendorService],
  bootstrap: [AppComponent]
})

export class AppModule { }
