<?php

header("Content-Type: application/json; charset=UTF-8");

header("Access-Control-Allow-Origin: *");

header("Access-Control-Allow-Methods: POST");

header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");

$input = file_get_contents("php://input");

$data = json_decode($input, true);

$accountId = null;

if (isset($data["accountNumber"])) {

    $accountId = $data["accountNumber"];

} elseif (isset($data["UserId"])) {

    $accountId = $data["UserId"];

}


if ($accountId) {

    $response = [

        "Success" => true,

        "Value" => [[

            "Id" => strval($accountId),

            "Money" => 1000,            

            "CurrencyId" => 87,          
            "Points" => 0,

            "Type" => 0,

            "Name" => "Main account",

            "OpenBonusStatus" => 0,

            "OpenBonusExists" => false

        ]]

    ];

} else {

    $response = [

        "Success" => false,

        "Error" => "Invalid or missing accountNumber"

    ];

}

echo json_encode($response, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

?>
