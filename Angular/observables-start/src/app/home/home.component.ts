import { Component, OnInit } from '@angular/core';
import {Observable} from "rxjs/Observable";
import 'rxjs/Rx'
import {Observer} from "rxjs/Observer";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  twoSecCounter;
  customObserver;
  customInter

  constructor() { }

  ngOnInit() {
    this.customObserver = Observable.create((observer: Observer<string>) => {
      setTimeout(()=>observer.next('first'),1000);
      setTimeout(()=>observer.next('second'),2000);
      setTimeout(()=>observer.next('third'),3000);
      setTimeout(()=>observer.complete(), 2200);
    })

    this.twoSecCounter = Observable.interval(2000).map((num:number)=> {return num * 2})
    this.twoSecCounter.subscribe((num:number) => console.log(num));
  }

  onStartObserve() {
    this.customObserver.subscribe(
      (data:string) => console.log(data),
      (error:string) => console.log(error),
      () => console.log("Completed")
    )
  }
}
