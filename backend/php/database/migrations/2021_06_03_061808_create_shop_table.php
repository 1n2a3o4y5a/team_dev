<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateShopTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('shop', function (Blueprint $table) {
            $table->bigIncrements('shop_id');
            $table->string('shop_name');
            $table->integer('prefecture_id')->unsigned();
            $table->foreign('prefecture_id')
            ->references('prefecture_id')
            ->on('m_prefecture')
            ->onDelete('cascade');
            $table->bigInteger('city_id')->unsigned();
            $table->foreign('city_id')
            ->references('city_id')
            ->on('m_city')
            ->onDelete('cascade');
            $table->string('adress');
            $table->string('nearest_station')->nullable();
            $table->text('description')->nullable();
            $table->timestamp('updated_at')->useCurrent()->nullable();
            $table->timestamp('created_at')->useCurrent()->nullable();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('shop');
    }
}
