import {Component, OnDestroy, OnInit} from '@angular/core';
import {UsersService} from "./users.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  user1Activated = false;
  user2Acitvated = false;
  constructor(private usersService: UsersService){}

  ngOnInit(){
    this.usersService.userActivatedSubject.subscribe((id:number) => {
      if(id===1)
        this.user1Activated = true;
      if(id===2)
        this.user2Acitvated = true;
    })
  }

}
