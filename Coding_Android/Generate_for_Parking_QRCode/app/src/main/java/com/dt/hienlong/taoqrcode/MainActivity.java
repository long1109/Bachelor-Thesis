package com.dt.hienlong.taoqrcode;

import android.graphics.Bitmap;
import android.os.Build;
import android.support.annotation.RequiresApi;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

import java.math.BigDecimal;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.math.BigInteger;
import java.security.SecureRandom;
import java.time.Instant;


import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;
import com.journeyapps.barcodescanner.BarcodeEncoder;

import org.json.JSONException;
import org.json.JSONObject;


public class MainActivity extends AppCompatActivity {
    EditText edtName,edtYear;
    Button btnClick;
    ImageView imageView;
    String aa="4917632450715632721768757419824479096209451061522489217370866229609231939526949048865885096127889468884988082822786198261549879571263755889554297528131827";
    String bb="8101265290001096908053897480281187994509015779944295061920807763823967797399977861769178873520852760993361820695662969316667749388117057342588050707807799";
    String a= "37694171648657005043281999931793983088550749995075284087474188163687754209859";
    //String b= "282940242616465515838557650309395738007";
    String c= "61585782000322565211213027396251628256519876094144898656255590243791531617141";
    String typeloai = "1";
    BigInteger dd1 = new BigInteger(aa,10);
    BigInteger nn1 = new BigInteger(bb,10);
    BigInteger d= new BigInteger(a, 10);
    //BigInteger e= new BigInteger(b,10);
    BigInteger n = new BigInteger(c, 10);



    public static String GETMD5(String input)
    {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(input.getBytes());
            return convertByteToHex(messageDigest);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }

    }

    private static String convertByteToHex(byte[] data) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < data.length; i++) {
            sb.append(Integer.toString((data[i] & 0xff) + 0x100, 16).substring(1));
        }
        return sb.toString();
    }

    public synchronized String encrypt(String message) {
        return (new BigInteger(message.getBytes())).modPow(dd1, nn1).toString();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //edtName = findViewById(R.id.edtName);
        //edtTruong = findViewById(R.id.edtTruong);
        //edtYear = findViewById(R.id.edtYear);
        //edtKey = findViewById(R.id.edtKey);
        btnClick = findViewById(R.id.btnClick);
        imageView = findViewById(R.id.imageView);


        btnClick.setOnClickListener(new View.OnClickListener() {
            @RequiresApi(api = Build.VERSION_CODES.O)
            @Override
            public void onClick(View v) {
                //String Name=edtName.getText().toString().trim();
                String Name="1412103";
                String Key3=" ";
                //String Truong=edtTruong.getText().toString().trim();
                //String Year=edtYear.getText().toString().trim();
                //String Year="";

                   long Key = Instant.now().getEpochSecond();
                    int Key2=(int) Key;
                    Key3= Integer.toString(Key2);


                //int Key2=(int) Key;
               // String Key3= Integer.toString(Key2);
                //int Key2=int

                String Truong=" ";
                //String Key=edtKey.getText().toString().trim();
                String hashedid = GETMD5(Name);
                String mahoa = encrypt(hashedid);


                JSONObject jsonObject = new JSONObject();

                try {
                    jsonObject.put("idkhachhang",Name);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                try {
                    jsonObject.put("rsaidkhachhang",mahoa);
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                try {
                    jsonObject.put("timestamp",Key3);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                try{
                    jsonObject.put("type", typeloai);

                }catch (JSONException e){
                    e.printStackTrace();
                }

                String qrstring = jsonObject.toString();


                if(qrstring != null){
                    MultiFormatWriter multiFormatWriter = new MultiFormatWriter();

                    try {
                        BitMatrix bitMatrix = multiFormatWriter.encode(qrstring, BarcodeFormat.QR_CODE, 1400, 1400
                        );
                        BarcodeEncoder barcodeEncoder = new BarcodeEncoder();
                        Bitmap bitmap = barcodeEncoder.createBitmap(bitMatrix);

                        imageView.setImageBitmap(bitmap);
                    } catch (WriterException e){
                        e.printStackTrace();
                    }



                }

            }
        });



    }
}
