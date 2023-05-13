import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-response',
  templateUrl: './response.component.html',
  styleUrls: ['./response.component.css']
})
export class ResponseComponent {
  data: any;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.dataUpdated.subscribe(response => {
      this.data = response;
    });
  }
}
