import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PayFarmerComponent } from './pay-farmer.component';

describe('PayFarmerComponent', () => {
  let component: PayFarmerComponent;
  let fixture: ComponentFixture<PayFarmerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PayFarmerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PayFarmerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
