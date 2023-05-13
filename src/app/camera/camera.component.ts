import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { WebcamImage, WebcamInitError, WebcamUtil } from 'ngx-webcam';
import { Observable, Subject } from 'rxjs';
import { DataService } from '../data.service';

@Component({
  selector: 'app-camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.css']
})
export class CameraComponent implements OnInit {
  
  @Output() getPicture = new EventEmitter<WebcamImage>();
  showWebcam = true;

  isCameraExist = true;
  captureImage  = '';

  errors: WebcamInitError[] = [];

  // webcam snapshot trigger
  private trigger: Subject<void> = new Subject<void>();
  private nextWebcam: Subject<boolean | string> = new Subject<boolean | string>();
  public webcamImage!: WebcamImage;

  constructor( private dataService: DataService ) { }

  ngOnInit(): void {
    WebcamUtil.getAvailableVideoInputs()
      .then((mediaDevices: MediaDeviceInfo[]) => {
        this.isCameraExist = mediaDevices && mediaDevices.length > 0;
      });
  }

  takeSnapshot(): void {
    this.trigger.next();

    let block = this.webcamImage.imageAsDataUrl.split(";");
    const base64ImageContent = this.webcamImage.imageAsDataUrl.split(',')[1];
    const byteArray = atob(base64ImageContent);
    const file = new File(
      [new Uint8Array([...byteArray].map(char => char.charCodeAt(0)))],
      'image.png',
      { type: 'image/png' }
    );

    this.dataService.updateData( file );
  }


  onOffWebCame() {
    this.showWebcam = !this.showWebcam;
  }

  handleInitError(error: WebcamInitError) {
    this.errors.push(error);
  }

  changeWebCame(directionOrDeviceId: boolean | string) {
    this.nextWebcam.next(directionOrDeviceId);
  }

  handleImage(webcamImage: WebcamImage) {
    this.webcamImage = webcamImage;
    //this.showWebcam = false;
    console.info('received webcam image', this.webcamImage);
  }

  get triggerObservable(): Observable<void> {
    return this.trigger.asObservable();
  }

  get nextWebcamObservable(): Observable<boolean | string> {
    return this.nextWebcam.asObservable();
  }

  b64toBlob(b64Data: any, contentType: string) {
    contentType = contentType || '';
    let sliceSize = 512;

    var byteCharacters = atob(b64Data); // window.atob(b64Data)
    var byteArrays = [];

    for (var offset = 0; offset < byteCharacters.length; offset += sliceSize) {
      var slice = byteCharacters.slice(offset, offset + sliceSize);

      var byteNumbers = new Array(slice.length);
      for (var i = 0; i < slice.length; i++) {
        byteNumbers[i] = slice.charCodeAt(i);
      }

      var byteArray = new Uint8Array(byteNumbers);

      byteArrays.push(byteArray);
    }

    return new Blob(byteArrays, {type: contentType});
  }
}
