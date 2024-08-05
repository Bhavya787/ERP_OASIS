import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowFarmersComponent } from './show-farmers.component';

describe('ShowFarmersComponent', () => {
  let component: ShowFarmersComponent;
  let fixture: ComponentFixture<ShowFarmersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowFarmersComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowFarmersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
