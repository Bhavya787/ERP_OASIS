import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RawMaterialsDeatailsComponent } from './raw-materials-deatails.component';

describe('RawMaterialsDeatailsComponent', () => {
  let component: RawMaterialsDeatailsComponent;
  let fixture: ComponentFixture<RawMaterialsDeatailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RawMaterialsDeatailsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RawMaterialsDeatailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
