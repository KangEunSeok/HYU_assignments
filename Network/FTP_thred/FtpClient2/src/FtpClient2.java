import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.net.Socket;

public class FtpClient2 {
  public static void main(String[] args ) {
    try {
      //access server
      int portNum;
      if (args.length != 1) {
    	portNum = 2020;
      }
      else {
        portNum = Integer.parseInt(args[0]);
        if (portNum < 1024) {
          System.out.println("Wrong prot Number");
        }
      }
      Socket socket = new Socket("127.0.0.1", portNum);
      String sentence, errorWrongcmd, errorNotFound;
      String [] sentenceWords;
      String curPath = "NoPath";
      errorWrongcmd =  "Wrong cmd try again.";
      errorNotFound = "Failed directory name is invalid.";
      // connect to server
      while (true) {
        BufferedWriter bufWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        sentence = inFromUser.readLine() + " " + curPath;
        if ("".equals(sentence)) {
          System.out.println(errorWrongcmd);
          continue;
        }
        sentenceWords = sentence.split("\\s");
        bufWriter.write(sentence);
        bufWriter.newLine();
        bufWriter.flush();
        if ("Done".equals(sentence)) {  // disconnection
          break;
        }
        // request about "CD" and get response
        if ("CD".equals(sentenceWords[0])) {
            InputStream in = socket.getInputStream();                       
            DataInputStream din = new DataInputStream(in);     
            int statusCode = din.readInt();
            int responseLength = din.readInt();
            if (statusCode == -1) {
              System.out.println(din.readUTF());
            }else {
              curPath = din.readUTF();
              System.out.println(curPath);    	
            }
        }
        // request about "LIST" and get response
        else if("LIST".equals(sentenceWords[0]) ) {
          InputStream in = socket.getInputStream();                       
          DataInputStream din = new DataInputStream(in);     
          int statusCode = din.readInt();
          int responseLength = din.readInt();
          String response = din.readUTF();
          String responses [] = response.split("\t");
          for(int i=0; i < responses.length;i++) {
            System.out.println(responses[i]);
          }
        }
        // request about "GET" and get response
        else if("GET".equals(sentenceWords[0])) {
          int len, data,statusCode;
          byte[] buffer = new byte[1024];                                     
          InputStream in = socket.getInputStream();                       
          DataInputStream din = new DataInputStream(in);    
          statusCode = din.readInt();
          data = din.readInt();             // get file size                     
          String filename = din.readUTF();  // get file name
          if (statusCode == -1) {           // error response 
            System.out.println(filename);
            continue;
          }
          FileOutputStream out = new FileOutputStream(filename);
          for(int i = data; i > 0; i--){   // save file to Client
        	len = in.read(buffer);
            out.write(buffer,0,len);
          }
          System.out.println("Received " + filename); 
          System.out.println(+ data +" kbytes");
          out.flush();
          out.close();
        }
        // request about "PUT" and get response
        else if("PUT".equals(sentenceWords[0])) { 
          InputStream in = socket.getInputStream();                       
          DataInputStream din = new DataInputStream(in); 	
          int statusCode;
          String currentPath = new java.io.File("").getCanonicalPath();  
          if (sentenceWords.length == 1) {  // get response about wrong cmd
              statusCode = din.readInt();
              String response = din.readUTF();
              System.out.println(response);
          }
          else{  // upload file to server
        	File file = new File(currentPath + "\\" + sentenceWords[1]);    
        	OutputStream out = socket.getOutputStream();               
            DataOutputStream dout = new DataOutputStream(out);
            int len;                          
            int data=0;                       
            byte[] buffer = new byte[1024];   
            if (file.isFile()) {  // find relative path file 
              FileInputStream fin = new FileInputStream(currentPath + "\\" +sentenceWords[1]); 
              String fileName = sentenceWords[1];
              while((len = fin.read(buffer))>0){   // calculate upload file size
                  data++;                        
              }
              fin.close();
              fin = new FileInputStream(sentenceWords[1]); 
              dout.writeInt(data);                   
              dout.writeUTF(fileName);       
              len = 0;
              for(int i = data; i>0; i--){      // upload file to server
                len = fin.read(buffer);        
                out.write(buffer,0,len);       
              }
              fin.close();
              out.flush();
              statusCode = din.readInt();
              String response = din.readUTF();
              System.out.println(response);
            }
            else {   // absolute path file
              file = new File(sentenceWords[1]);
              if (file.isFile()) {
                FileInputStream fin = new FileInputStream(sentenceWords[1]);  
                String [] parseFileName = sentenceWords[1].split("\\\\");
                String fileName = parseFileName[parseFileName.length-1];
                while((len = fin.read(buffer))>0){   // calculate upload file size
                    data++;                        
                }
                fin.close();
                fin = new FileInputStream(sentenceWords[1]); 
                dout.writeInt(data);                   
                dout.writeUTF(fileName);       
                len = 0;
                for(int i = data; i>0; i--){      // upload file to server
                  len = fin.read(buffer);        
                  out.write(buffer,0,len);       
                }
                fin.close();
                out.flush();
                statusCode = din.readInt();
                String response = din.readUTF();
                System.out.println(response);
              }
              else {  // if file doesn't exist
            	dout.writeInt(-1);
            	statusCode = din.readInt();
                String response = din.readUTF();
                System.out.println(response);
              }
            } 
          }
        }
        // get Wrong cmd response
        else {
          InputStream in = socket.getInputStream();                       
          DataInputStream din = new DataInputStream(in);    
          String message = din.readUTF();
          System.out.println(message);	  	
        }
      } 
      socket.close();   
    }
    catch( Exception e ){
            e.printStackTrace();
        }
    }
}
