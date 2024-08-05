import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MilkBifurcationComponent } from './milk-bifurcation.component';

describe('MilkBifurcationComponent', () => {
  let component: MilkBifurcationComponent;
  let fixture: ComponentFixture<MilkBifurcationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MilkBifurcationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MilkBifurcationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
