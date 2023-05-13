import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CameraComponent } from './camera/camera.component';
import { WebcamModule } from 'ngx-webcam';
import { MatToolbarModule } from '@angular/material/toolbar';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HeaderComponent } from './header/header.component';
import {MatIconModule} from '@angular/material/icon';
import { FooterComponent } from './footer/footer.component';
import { ResponseComponent } from './response/response.component';
import {MatProgressBarModule} from "@angular/material/progress-bar";
import {MatButtonModule} from "@angular/material/button";
import {HttpClientModule} from "@angular/common/http";
import {DataService} from "./data.service"

@NgModule({
  declarations: [
    AppComponent,
    CameraComponent,
    HeaderComponent,
    FooterComponent,
    ResponseComponent,
  ],
  imports: [
    BrowserModule,
    MatToolbarModule,
    AppRoutingModule,
    WebcamModule,
    BrowserAnimationsModule,
    MatIconModule,
    MatProgressBarModule,
    MatButtonModule,
    HttpClientModule
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
