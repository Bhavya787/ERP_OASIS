import { Component } from '@angular/core';
import {} from '@fortawesome/free-brands-svg-icons'
import {faUser} from '@fortawesome/free-solid-svg-icons'
import {faFile} from '@fortawesome/free-solid-svg-icons'
import {faIdCard} from '@fortawesome/free-solid-svg-icons'
import {faMoneyBillAlt} from '@fortawesome/free-solid-svg-icons'
import {faRegistered} from '@fortawesome/free-solid-svg-icons'
import {faAddressBook} from '@fortawesome/free-solid-svg-icons'
import {faChartBar} from '@fortawesome/free-solid-svg-icons'
import {faCreditCard} from '@fortawesome/free-solid-svg-icons'
import {faChartArea} from '@fortawesome/free-solid-svg-icons'
import {faChartPie} from '@fortawesome/free-solid-svg-icons'


import {faAccessibleIcon} from '@fortawesome/free-brands-svg-icons'

import {} from '@fortawesome/free-regular-svg-icons'






@Component({
  selector: 'app-root', 
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  faUser = faUser;
  faFile = faFile;
  faIdCard = faIdCard;
  faMoneyBillAlt = faMoneyBillAlt;
  faRegistered = faRegistered;
  faAddressBook = faAddressBook;
  faChartBar = faChartBar;
  faCreditCard = faCreditCard;
  faAccessibleIcon = faAccessibleIcon;
  faChartArea = faChartArea;
  faChartPie = faChartPie;
}
