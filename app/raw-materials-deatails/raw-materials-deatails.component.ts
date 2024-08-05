import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-raw-materials-deatails',
  templateUrl: './raw-materials-deatails.component.html',
  styleUrls: ['./raw-materials-deatails.component.scss']
})
export class RawMaterialsDeatailsComponent implements OnInit {
  
  data: any[] = [];
  // columns: string[] = [];
  columns: string[] = [ 'MilkCM500RoleQuan',
            'MilkCM200RoleQuan',
            'MilkTM500RoleQuan',
            'MilkTM200RoleQuan',
            'Lassi200RoleQuan',
            'LassiCUP200cupQuan',
            'LassiMANGOCUP200cupQuan',
            'Dahi200MLRoleQuan',
            'Dahi500MLRoleQuan',
            'Dahi2LTBucketQuan',
            'Dahi5LTBucketQuan',
            'Dahi10LTBucketQuan',
            'Dahi2LT1_5BucketQuan',
            'Dahi5LT1_5BucketQuan',
            'Dahi10LT1_5BucketQuan',
            'ButtermilkRoleQuan',
            'Khova500TinQuan',
            'Khoya1000TinQuan',
            'Shrikhand100TinQuan',
            'Shrikhand250TinQuan',
            'Ghee200TinQuan',
            'Ghee500TinQuan',
            'Ghee15LTTinQuan',
            'PaneerlooseQuan',
            'khovalooseQuan',
            'LASSICUPFOILQuan',
            'IFFFLAVERMANGOQuan',
            'IFFFLAVERVANILLAQuan',
            'CULTUREAMAZIKAQuan',
            'CULTUREDANISKOQuan',
            'CULTUREHRQuan',
            'LIQUIDSOAPQuan',
            'COSSODAQuan',
            'KAOHQuan'];
  // rawMaterials: any[] = ['name', 'quantity', 'price'];
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.fetchData();
  }
  fetchData(): void {
    this.http.get<any[]>('http://127.0.0.1:5000/get-raw-materials')
      .subscribe(response => {
        this.data = response;
      }, error => {
        console.error('Error fetching data', error);
      });

}
}



