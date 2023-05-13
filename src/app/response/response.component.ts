import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-response',
  templateUrl: './response.component.html',
  styleUrls: ['./response.component.css']
})
export class ResponseComponent {

  private readonly _apiUrl = "http://localhost:5000/search";

  constructor(private readonly _http: HttpClient) { }

  getApiResponse() {
    this._http.get<any>(this._apiUrl).subscribe((response: string) => {
      console.log(response); // Log the response string to the console for debugging purposes
      // Do something with the response string here
    });
  }

}

