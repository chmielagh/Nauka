import {Component, EventEmitter, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-game-control',
  templateUrl: './game-control.component.html',
  styleUrls: ['./game-control.component.css']
})
export class GameControlComponent implements OnInit {
  counter: number;
  intervalHandler;
  @Output() currentNumber = new EventEmitter<{num: number}>();

  constructor() {
    this.counter = 0;
  }

  ngOnInit() {
  }

  startGame() {
    this.intervalHandler = setInterval(() => {this.currentNumber.emit({num: ++this.counter}); }, 1000);
  }

  stopGame() {
    clearInterval(this.intervalHandler);
  }

}
