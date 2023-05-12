import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { WebcamImage, WebcamInitError, WebcamUtil } from 'ngx-webcam';
import { Observable, Subject } from 'rxjs';

@Component({
  selector: 'app-camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.css']
})
export class CameraComponent implements OnInit {
  @Output() getPicture = new EventEmitter<WebcamImage>();
  showWebcam = true;
  isCameraExist = true;

  errors: WebcamInitError[] = [];

  // webcam snapshot trigger
  private trigger: Subject<void> = new Subject<void>();
  private nextWebcam: Subject<boolean | string> = new Subject<boolean | string>();

  constructor() { }


  ngOnInit(): void {
    WebcamUtil.getAvailableVideoInputs()
      .then((mediaDevices: MediaDeviceInfo[]) => {
        this.isCameraExist = mediaDevices && mediaDevices.length > 0;
      });
  }

  takeSnapshot(): void {
    this.trigger.next();

    // Get a reference to the video element and canvas element
    const video = document.getElementById('video') as HTMLVideoElement;
    const canvas = document.createElement('canvas') as HTMLCanvasElement;

    // Set the canvas dimensions to match the video element
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Draw the current frame of the video onto the canvas
    const context = canvas.getContext('2d');
    if (context) {
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
      const imageDataUrl = canvas.toDataURL('image/jpeg');
      // ...rest of the code...
    } else {
      console.error('Canvas context is null');
    }

    // Convert the canvas image to a base64-encoded string
    const imageDataUrl = canvas.toDataURL('image/jpeg');

    // Send the base64-encoded image to the Google Images search API endpoint
    fetch('https://www.googleapis.com/customsearch/v1', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer AIzaSyDinCCdr2TB0JujH-skL-AMj1n5R6UwAC8',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        q: 'search term',
        searchType: 'image',
        imgSize: 'medium',
        imgType: 'photo',
        imgDominantColor: 'black',
        cx: '93d48a0cd46fd4c86',
        safe: 'high',
        num: 1,
        start: 1,
        exactTerms: 'search term',
        imgUrl: imageDataUrl,
        fileFormat: 'jpg'
      })
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('API Error');
        }
      })
      .then(data => {
        if (data.items && data.items.length > 0) {
          const img = document.createElement('img');
          img.src = data.items[0].link;
          document.body.appendChild(img);
        }
      })
      .catch(error => {
        console.error(error);
      });
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
    this.getPicture.emit(webcamImage);
    this.showWebcam = false;
  }

  get triggerObservable(): Observable<void> {
    return this.trigger.asObservable();
  }

  get nextWebcamObservable(): Observable<boolean | string> {
    return this.nextWebcam.asObservable();
  }

}
