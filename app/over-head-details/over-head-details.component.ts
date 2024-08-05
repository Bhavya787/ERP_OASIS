import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-over-head-details',
  templateUrl: './over-head-details.component.html',
  styleUrls: ['./over-head-details.component.scss']
})
export class OverHeadDetailsComponent implements OnInit {
  data: any[] = [];
  columns: string[] = ['date', 'expense_name', 'expense_amt', 'status'];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.fetchData();
  }

  fetchData(): void {
    this.http.get<any[]>('http://127.0.0.1:5000/showoverhead')
      .subscribe(response => {
        this.data = response;
      }, error => {
        console.error('Error fetching data', error);
      });
  }

}

