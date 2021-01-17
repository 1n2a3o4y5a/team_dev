import Vue from "vue";
import VueRouter from "vue-router";
// import Home from '../views/Home.vue'
import MainLayout from "../component/rayout/MainLayout.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "mainlayout",
    component: MainLayout
    // children: [
    //   {
    //     path: 'shops',
    //     name: 'shops',
    //     component: ShopIndex
    //   },
    //   {
    //     path: 'postShop',
    //     path: 'postShop',
    //     component: postShopIndex
    //   }
    // ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
