import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BuyMilkComponent } from './buy-milk.component';

describe('BuyMilkComponent', () => {
  let component: BuyMilkComponent;
  let fixture: ComponentFixture<BuyMilkComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BuyMilkComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BuyMilkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
