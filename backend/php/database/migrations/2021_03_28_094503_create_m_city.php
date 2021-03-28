<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateMCity extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('m_city', function (Blueprint $table) {
            $table->bigInteger('city_id')->unsigned()->primary();
            $table->foreign('prefecture_id')->references('prefecture_id')->on('m_prefecture')->onDelete('cascade');
            $table->string('name')->default('');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('m_city');
    }
}
