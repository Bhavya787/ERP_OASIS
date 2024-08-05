import { Component, OnInit } from '@angular/core';
    import { Injectable } from '@angular/core';
    import { HttpClient, HttpHeaders } from '@angular/common/http';
    import { Observable } from 'rxjs';
    
    @Injectable({
      providedIn: 'root'
    })
    export class DataService {
    
      private apiUrl = 'http://localhost:4200/manage';  // Adjust the URL according to your backend
    
      constructor(private http: HttpClient) { }
    
      postTruckData(truckData: any): Observable<any> {
        const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
        return this.http.post(this.apiUrl, truckData, { headers: headers });
      }
    }
    
    @Component({
      selector: 'app-manage-trucks',
      templateUrl: './manage-trucks.component.html'
    })
    export class ManageTrucksComponent {
      truckData = {
        truckNumber: '',
        driverName: '',
        source: '',
        destination: '',
        truckModel: '',
        kilometers: '0'
      };
    
      constructor(private dataService: DataService) { }
    
      onSubmit() {
        this.dataService.postTruckData(this.truckData).subscribe(response => {
          alert(response.message);
        }, error => {
          alert('Error: ' + error.error.error);
        });
      }
    }