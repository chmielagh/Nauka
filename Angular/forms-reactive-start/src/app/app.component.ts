import {Component, OnInit} from '@angular/core';
import {FormArray, FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  signupForm: FormGroup;
  genders = ['male', 'female'];
  forbiddenHobbies = ['Poker', "Hazard"];

  ngOnInit() {
    this.signupForm = new FormGroup({
      'userdata': new FormGroup({
        'username': new FormControl(null, Validators.required),
        'email': new FormControl(null, [Validators.required, Validators.email]),
      }),
      'gender': new FormControl("male"),
      'hobbies': new FormArray([])
    })
  }

  onSubmit(){
    console.log(this.signupForm);
  }

  onAddHobby(){
    (<FormArray>this.signupForm.get('hobbies')).push(new FormControl(null, [Validators.required, this.forbiddenHobby.bind(this)]));
  }

  forbiddenHobby(control: FormControl): {[s: string]: boolean}{
    if(this.forbiddenHobbies.indexOf(control.value) !== -1){
      return {'hobbyIsForbidden': true}
    }
    return null;
  }
}



