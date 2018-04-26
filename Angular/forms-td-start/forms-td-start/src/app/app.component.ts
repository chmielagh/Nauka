import {Component, ViewChild} from '@angular/core';
import {NgForm, NgModel} from "@angular/forms";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  @ViewChild('f') form: NgForm;
  username:string = "Def";
  answer: string = "No answer";
  genders: string[] = ["male", "female"];

  suggestUserName() {
    const suggestedName = 'Superuser';
    this.form.form.patchValue({userData: {username: suggestedName}});
  }

  suggestEmail(username: NgModel){
    console.log(username);
    this.form.form.patchValue({userData: {email: username.value + '@whirly.pl'}})
  }

  onSubmit(){
    console.log(this.form);
    this.form.reset({userData: {email: '@whirly.pl'}});
  }


}
