import { ComponentFixture, TestBed } from '@angular/core/testing';
import { OverHeadDetailsComponent } from './over-head-details.component';

describe('OverHeadDetailsComponent', () => {
  let component: OverHeadDetailsComponent;
  let fixture: ComponentFixture<OverHeadDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OverHeadDetailsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OverHeadDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
