import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ManageTrucksComponent } from './manage-trucks.component';

describe('ManageTrucksComponent', () => {
  let component: ManageTrucksComponent;
  let fixture: ComponentFixture<ManageTrucksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ManageTrucksComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ManageTrucksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
