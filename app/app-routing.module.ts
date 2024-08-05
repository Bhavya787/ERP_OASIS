import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BuyMilkComponent } from './buy-milk/buy-milk.component';
import { LogisticsDetailsComponent } from './logistics-details/logistics-details.component';
import { LogisticsComponent } from './logistics/logistics.component';
import { ManageTrucksComponent } from './manage-trucks/manage-trucks.component';
import { MilkBifurcationComponent } from './milk-bifurcation/milk-bifurcation.component';
import { OverHeadDetailsComponent } from './over-head-details/over-head-details.component';
import { OverheadComponent } from './overhead/overhead.component';
import { PayFarmerComponent } from './pay-farmer/pay-farmer.component';
import { ProductPricesComponent } from './product-prices/product-prices.component';
import { RawMaterialsDeatailsComponent } from './raw-materials-deatails/raw-materials-deatails.component';
import { RawMaterialsComponent } from './raw-materials/raw-materials.component';
import { RegisterFarmerComponent } from './register-farmer/register-farmer.component';
import { RegisterVendorComponent } from './register-vendor/register-vendor.component';
import { SellProductsComponent } from './sell-products/sell-products.component';
import { ShowFarmersComponent } from './show-farmers/show-farmers.component';
import { ShowVendorsComponent } from './show-vendors/show-vendors.component';
import { TruckDetailsComponent } from './truck-details/truck-details.component';
import { UseRawMaterialComponent } from './use-raw-material/use-raw-material.component';
import { VendorStatusComponent } from './vendor-status/vendor-status.component';
import { VendorPaymentsComponent } from './vendor-payments/vendor-payments.component';
import { VendorTransactionsComponent } from './vendor-transactions/vendor-transactions.component';
import { ProductProductionComponent } from './product-production/product-production.component';

const routes: Routes = [

  {
    component:RegisterFarmerComponent,
    path:'RegisterFarmer'
  },
  {
    component:BuyMilkComponent,
    path:'BuyMilk'
  },
  {
    component:ShowFarmersComponent,
    path:'ShowFarmers'
  },
  {
    component:PayFarmerComponent,
    path:'PayFarmer'
  },
  {
    component:MilkBifurcationComponent,
    path:'MilkBifurcation'
  },
  {
    component:RegisterVendorComponent,
    path:'RegisterVendor'
  },
  {
    component:ShowVendorsComponent,
    path:'ShowVendors'
  },
  {
    component:ProductPricesComponent,
    path:'ProductPrices'
  },
  {
    component:SellProductsComponent,
    path:'SellProducts'
  },
  {
    component:VendorStatusComponent,
    path:'VendorStatus'
  },
  {
    component:ManageTrucksComponent,
    path:'ManageTrucks'
  },
  {
    component:TruckDetailsComponent,
    path:'TruckDetails'
  },
  {
    component:OverheadComponent,
    path:'Overhead'
  },
  {
    component:OverHeadDetailsComponent,
    path:'OverheadDetails'
  },
  {
    component:LogisticsComponent,
    path:'Logistics'
  },
  {
    component:LogisticsDetailsComponent,
    path:'LogisticsDetails'
  },
  {
    component:RawMaterialsComponent,
    path:'RawMaterials'
  },
  {
    component:UseRawMaterialComponent,
    path:'UseRawMaterials'
  },
  {
    component:RawMaterialsDeatailsComponent,
    path:'RawMaterialsDetails'
  },
  {
    component:VendorPaymentsComponent,
    path:'VendorPayments'
  },
  {
    component:VendorTransactionsComponent,
    path:'VendorTransactions'
  },
  {
    component:ProductProductionComponent,
    path:'ProductProduction'
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
