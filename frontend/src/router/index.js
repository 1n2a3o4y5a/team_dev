import Vue from "vue";
import VueRouter from "vue-router";
import MainLayout from "@/component/rayout/MainLayout";
import ShopIndex from "@/component/pages/shop/ShopIndex"
import PostShopIndex from "@/component/pages/postshop/PostShopIndex"
import ShopDetailIndex from "@/component/pages/shop/shopdetail/ShopDetailIndex"
// import { component } from "vue/types/umd";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "mainlayout",
    component: MainLayout,
    children: [
      {
        path: 'shops',
        name: 'shops',
        component: ShopIndex,
        children: [
          {
            path: 'detail',
            name: 'detail',
            component: ShopDetailIndex
          }
        ]
      },
      {
        path: 'postShop',
        name: 'postShop',
        component: PostShopIndex
      }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
