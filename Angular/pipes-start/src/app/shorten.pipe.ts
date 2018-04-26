import {Pipe, PipeTransform} from "@angular/core";

@Pipe({name:'shorten'})
export class ShortenPipe implements PipeTransform{
  transform(value: any, ...args: any[]): any {
    const parts: string[] = value.split(" ");
    let result:string = '';
    for(let part of parts)
      result+=part.slice(0,1)+'. ';
    return result;
  }

}
