import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OverheadComponent } from './overhead.component';

describe('OverheadComponent', () => {
  let component: OverheadComponent;
  let fixture: ComponentFixture<OverheadComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OverheadComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OverheadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
