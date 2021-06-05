<?php

namespace App\Repositories\Shop;

use App\Shop;

class ShopDataAccessRepository implements ShopDataAccessRepositoryInterface
{
    public function getAll()
    {
        return Shop::all();
    }
}
