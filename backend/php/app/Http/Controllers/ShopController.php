<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Repositories\ShopDataAccessRepositoryInterface as ShopDataAccess;

class ShopController extends Controller
{
    protected $Shop;

    public function __construct(ShopDataAccess $ShopDataAccess)
    {
        $this->Shop = $ShopDataAccess;
    }

    public function index() 
    {

        $data = $this->Shop->getAll();

        dd($data);
    }  
}
