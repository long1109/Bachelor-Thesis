package com.dt.hienlong.muonxe_guitra;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Build;
import android.support.annotation.RequiresApi;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

//import com.dt.hienlong.muonxe_luu.R;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;
import com.journeyapps.barcodescanner.BarcodeEncoder;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.time.Instant;

public class MainActivity extends AppCompatActivity {
    private static final String FILE_NME ="example.txt";

    //EditText mEditText;
    //EditText edt1;
    //EditText edt2;
    //EditText edt3;
    Button   Button1;
    ImageView Imageview;
    String aa="4917632450715632721768757419824479096209451061522489217370866229609231939526949048865885096127889468884988082822786198261549879571263755889554297528131827";
    String cc="8101265290001096908053897480281187994509015779944295061920807763823967797399977861769178873520852760993361820695662969316667749388117057342588050707807799";
    String a= "37694171648657005043281999931793983088550749995075284087474188163687754209859";
    //String b= "282940242616465515838557650309395738007";
    String c= "61585782000322565211213027396251628256519876094144898656255590243791531617141";
    String f="183469043136488357765160417922964354333";
    String e="79710425938967830468396137237578837744486449057068804209709627857536329300881";

    String Name ="1412103";
    //String Key3 ="";
    String Type = "2";
    String Type2 = "3";
    //String text = "1";
    //String text2="";
    //JSONObject jsonObject1 = null;

    BigInteger d= new BigInteger(aa, 10);
    //BigInteger e= new BigInteger(b,10);
    BigInteger n = new BigInteger(cc, 10);
    BigInteger enhaxe=new BigInteger(f,10);
    BigInteger nnhaxe=new BigInteger(e,10);


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
        return (new BigInteger(message.getBytes())).modPow(d, n).toString();
    }
    public synchronized String decrypt(String message) {
        return new String ((new BigInteger(message)).modPow(enhaxe, nnhaxe).toByteArray());
    }




    @RequiresApi(api = Build.VERSION_CODES.O)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //mEditText = findViewById(R.id.edtext);
        //edt1 = findViewById(R.id.edtext1);
        //edt2 = findViewById(R.id.edtext2);
        //edt3 = findViewById(R.id.edtext3);
        Button1 = findViewById(R.id.button1);
        Imageview = findViewById(R.id.imageview);
        //Button2 = findViewById(R.id.button2);
        final IntentIntegrator intentIntegrator = new IntentIntegrator(this);
        //long Key= 0;
        //if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
        //   Key = Instant.now().getEpochSecond();
        //}
        // int Key2=(int) Key;
        // Key3= Integer.toString(Key2);
        Button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                intentIntegrator.initiateScan();
            }
        });


    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        IntentResult result = IntentIntegrator.parseActivityResult(requestCode,resultCode,data);
        if(result != null) {

            //JSONObject jsonObject1 = null;

            if(result.getContents() == null  ) {
                Toast.makeText(this, "Cancelled", Toast.LENGTH_LONG).show();
            } else {

                String text3=" ";
                text3 = result.getContents().toString();
                FileOutputStream fos = null;
                    try {
                        fos = openFileOutput(FILE_NME, MODE_PRIVATE);
                        fos.write(text3.getBytes());

                        //mEditText.getText().clear();
                        Toast.makeText(this, "savedto" + getFilesDir() + "/" + FILE_NME, Toast.LENGTH_LONG).show();
                    } catch (FileNotFoundException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    } finally {
                        if (fos != null) {
                            try {
                                fos.close();
                            } catch (IOException e) {
                                e.printStackTrace();
                            }
                        }
                    }




            }
        } else {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }




    public  void load(View v) {
        FileInputStream fis =null;
        long Key3= Instant.now().getEpochSecond();
        int Key2 = (int) Key3;
        String Key = Integer.toString(Key2);
        String text2=" ";
        String text3=" ";
        String text4=" ";
        String text5=" ";




        try {
            fis=openFileInput(FILE_NME);
            InputStreamReader isr = new InputStreamReader(fis);
            BufferedReader br = new BufferedReader(isr);
            StringBuilder sb = new StringBuilder();
            String text;
            while ((text = br.readLine()) != null){
                sb.append(text).append("");

            }
            String hashedid = GETMD5(Name);//nguoi muon
            String mahoa = encrypt(hashedid);
            //mEditText.setText(sb.toString());
            try {
                JSONObject jsonObject2 = new JSONObject(sb.toString());
                text2 = jsonObject2.getString("idnhaxe");
                text3 = jsonObject2.getString("ghichu");
                text4 = jsonObject2.getString("idkhachhang");
                text5 = jsonObject2.getString("rsaidkhachhang");//nguoi cho muon
            }catch (JSONException e1) {
                Toast.makeText(this, "Cancelledlolll", Toast.LENGTH_LONG).show();
                e1.printStackTrace();
            }

            JSONObject jsonObject = new JSONObject();


            try {
                jsonObject.put("idkhachhang",text4);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            try {
                jsonObject.put("rsaidkhachhang",text5);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            try {
                jsonObject.put("idnhaxe",text2);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            try {
                jsonObject.put("ghichu",text3);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            try {
                jsonObject.put("idkhmuon",Name);//nguoi muon la 1412103
            } catch (JSONException e) {
                e.printStackTrace();
            }
            try {
                jsonObject.put("rsaidkhmuon",mahoa);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            try {
                jsonObject.put("type",Type2);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            try {
                jsonObject.put("timestamp",Key);
            } catch (JSONException e) {
                e.printStackTrace();
            }



            String qrstring = jsonObject.toString();
            if(qrstring != null){
                MultiFormatWriter multiFormatWriter = new MultiFormatWriter();

                try {
                    BitMatrix bitMatrix = multiFormatWriter.encode(qrstring, BarcodeFormat.QR_CODE, 700, 700
                    );
                    BarcodeEncoder barcodeEncoder = new BarcodeEncoder();
                    Bitmap bitmap = barcodeEncoder.createBitmap(bitMatrix);
                    Imageview.setImageBitmap(bitmap);
                } catch (WriterException e){
                    e.printStackTrace();
                }



            }





        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }finally {
            if(fis != null){
                try {
                    fis.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }


}
