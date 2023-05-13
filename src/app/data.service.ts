import { Injectable, EventEmitter } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class DataService {
  private apiUrl = 'http://localhost:5000/search';
  public dataUpdated: EventEmitter<any> = new EventEmitter();

  constructor(private http: HttpClient) { }

  fetchData(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

  updateData( imagedata : any ) {
      
    const formData = new FormData();
    formData.append('image', imagedata);

    fetch( this.apiUrl, {
      method: 'POST',
      body: formData
    })
    .then ( response => response.json() )
    .then ( response => {
      console.log ( response )
      this.dataUpdated.emit ( response.message );
    })
    .catch(error => {
      console.error('Error:', error);
    });    
  }
}
