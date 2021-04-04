<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use GuzzleHttp\Client;
use App\Models\MasterPrefecture;
use App\Models\MasterCity;


class MasterCitySeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run(Client $client, MasterPrefecture $m_prefecture, MasterCity $m_city)
    {
        $m_prefecture = $m_prefecture->all();
        foreach ($m_prefecture->pluck('prefecture_id') as $id) {
            $prefecture_id = (strlen($id) == 1) ? sprintf('%02d', $id) : (string) $id;
            $api = 'https://www.land.mlit.go.jp/webland/api/CitySearch?area=' .str_pad($prefecture_id, 2, 0, STR_PAD_LEFT);
            $respone_datas = $client->request('GET', $api);
            $respone_bodys = json_decode($respone_datas->getBody()->getContents(), true);
            if ($respone_bodys['status'] === 'OK') {
                foreach ($respone_bodys['data'] as $respone_body) {
                    $m_city->create([
                        'city_id'       => (integer) $respone_body['id'],
                        'prefecture_id' => $id,
                        'name'          => $respone_body['name']
                    ]);
                }
            }
        }
    }
}
