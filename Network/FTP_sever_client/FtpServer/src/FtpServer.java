import java.io.BufferedReader;
import java.io.File;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Properties;

public class FtpServer {
  /* 
   * find parent path method
   * parsing about "\" and return parent path
  */	
  public String getParentPath() { 
    String [] parsePath = System.getProperty("user.dir").split("\\\\");
    String parentPath = parsePath[0];
	for (int i=1; i< parsePath.length-1;i++) {
      parentPath = parentPath + "\\" + parsePath[i];
	}
    return parentPath;
  }
  /* 
   * find directory & file list about input path
   * each directory & file add "\t" for parsing 
   * if is a directory add "-" and is a file add "file size" 
   */
  public String findLISTandResponse(File dir) {  
    String resultList = "";
	File[] fileList = dir.listFiles(); 
    for(int i = 0 ; i < fileList.length ; i++){
  	  File file = fileList[i];
      String fileSize = "-";
  	  if (file.isFile()) {
  	    fileSize = String.valueOf(file.length());
  	  }
  	  resultList = resultList + file.getName() + " " + fileSize + "\t";
  	}
    return resultList;
  }
  
  public static void main(String[] args ) {
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
    //server always on and response to client request.
	try {
      ServerSocket serverSocket = new ServerSocket(portNum);
      String initialPath =  new java.io.File("").getCanonicalPath();
      // accept to client socket
      while (true) {
        Socket clientSocket = serverSocket.accept();
        FtpServer serve = new FtpServer();
        String response, request;
        String errorResponse = "Failed directory name is invalid.";
        String errorWrongcmd = "Wrong cmd try again.";
        // define response about each client request.
        while(true) {
          BufferedReader in = new BufferedReader( new InputStreamReader( clientSocket.getInputStream()));
          request = in.readLine();	
          String[] requestWords = request.split("\\s");
          // for disconnect to client and server 
          if("Done".equals(requestWords[0])) {
        	Properties prop = System.getProperties();
        	prop.setProperty("user.dir", initialPath);
            clientSocket.close();
            break;
          }
          /* responses about CD request
           * response return values are status code, response length, response value
           */
          else if("CD".equals(requestWords[0])) {
        	OutputStream out = clientSocket.getOutputStream();               
        	DataOutputStream dout = new DataOutputStream(out);
        	int statusCode = 1;
        	// response about "CD" or "CD ." request
        	if(requestWords.length == 1 || ".".equals(requestWords[1])) {
        	  //String currentPath = new java.io.File("").getCanonicalPath();
        	  String currentPath = System.getProperty("user.dir");
        	  dout.writeInt(statusCode);
        	  dout.writeInt(currentPath.length());
        	  dout.writeUTF(currentPath);
        	}
        	// response about "CD .." request
        	else if ("..".equals(requestWords[1])){  
        	  String parentPath = serve.getParentPath();
        	  Properties prop = System.getProperties();
        	  prop.setProperty("user.dir", parentPath);
        	  parentPath = System.getProperty("user.dir");
        	  dout.writeInt(statusCode);
        	  dout.writeInt(parentPath.length());
        	  dout.writeUTF(parentPath);
        	}
        	// response about "CD path" request
            else { 
              String curPath = System.getProperty("user.dir") + "\\" + requestWords[1];
              File dir = new File(curPath); 
              if (dir.isDirectory()) { // response about "CD relative path"
            	Properties prop = System.getProperties();
                prop.setProperty("user.dir", curPath);
                //String currentPath = new java.io.File("").getCanonicalPath();
                String currentPath = System.getProperty("user.dir");
                dout.writeInt(statusCode);
          	    dout.writeInt(currentPath.length());
          	    dout.writeUTF(currentPath);
              }
              else {  // response about "CD absolute path"
            	dir = new File(requestWords[1]);  
            	if (dir.isDirectory()) {
            	  Properties prop = System.getProperties();
                  prop.setProperty("user.dir", requestWords[1]);
                  //String currentPath = new java.io.File("").getCanonicalPath();
                  String currentPath = System.getProperty("user.dir");
                  dout.writeInt(statusCode);
              	  dout.writeInt(currentPath.length());
              	  dout.writeUTF(currentPath);
            	}
            	else {  // error response about "Wrong path" 
                  statusCode = -1; 
            	  dout.writeInt(statusCode);
            	  dout.writeInt(errorResponse.length());
            	  dout.writeUTF(errorResponse);
            	}
              } 
        	}
        	out.flush();
          }
          /* responses about LIST request
           * response return values are status code, response length, response value
          */
          else if("LIST".equals(requestWords[0])) {
        	OutputStream out = clientSocket.getOutputStream();               
        	DataOutputStream dout = new DataOutputStream(out);
        	int statusCode = 1;
        	// response about "LIST .", "LIST" request
            if (requestWords.length == 1 || ".".equals(requestWords[1])){  
        	  File dir = new File(System.getProperty("user.dir"));
              String fileList = serve.findLISTandResponse(dir);
              dout.writeInt(statusCode);
              dout.writeInt(fileList.length());
              dout.writeUTF(fileList);
        	}
        	// response about "LIST .." request
        	else if ("..".equals(requestWords[1])) { 
        	  String parentPath = serve.getParentPath();
          	  File dir = new File(parentPath);
          	  String fileList = serve.findLISTandResponse(dir);
           	  dout.writeInt(statusCode);
              dout.writeInt(fileList.length());
              dout.writeUTF(fileList);
       	    }
        	// response about "LIST relative path" and "LIST absolute path" request
        	else { 
        	  String curPath = System.getProperty("user.dir") + "\\" + requestWords[1];
        	  File dir = new File(curPath);
        	  if (dir.isDirectory()) { // about relative path
        		String fileList = serve.findLISTandResponse(dir);
        		dout.writeInt(statusCode);
                dout.writeInt(fileList.length());
                dout.writeUTF(fileList);
           	
        	  }
        	  else { // about absolute path
        	    File dir1 = new File(requestWords[1]);
                if (dir1.isDirectory()) {
                  String fileList = serve.findLISTandResponse(dir1);
                  dout.writeInt(statusCode);
                  dout.writeInt(fileList.length());
                  dout.writeUTF(fileList);
            	}
                else {  //error response about "Wrong path" 
            	  statusCode = -1;
                  dout.writeInt(statusCode);
                  dout.writeInt(errorResponse.length());
                  dout.writeUTF(errorResponse);
               	}			  
        	  }
        	}
        	out.flush();
          }
          /* responses about GET request
           * response return values are status code, file size, file name, file response value
           */
          else if("GET".equals(requestWords[0])) {    
        	OutputStream out = clientSocket.getOutputStream();               
        	DataOutputStream dout = new DataOutputStream(out);
        	int statusCode = 1;
        	String currentPath = System.getProperty("user.dir");
        	// error response about "Wrong cmd"
        	if (requestWords.length == 1) {   
              statusCode = -1;
        	  dout.writeInt(statusCode);
        	  dout.writeInt(errorWrongcmd.length());
              dout.writeUTF(errorWrongcmd);
              out.flush();
        	}
        	// find file and response file about "GET file name" or "GET file path" request
        	else {
              byte[] buffer = new byte[1024];   
              int len;                          
              int data=0;                       
              File file = new File(currentPath + "\\" +requestWords[1]);
        	  if (file.isFile()) {
        		FileInputStream fin = new FileInputStream(currentPath + "\\" +requestWords[1]);
                String fileName = requestWords[1];
                while((len = fin.read(buffer))>0){  // calculate file size
                    data++;                        
                  }
                fin.close();
                fin = new FileInputStream(currentPath + "\\" +requestWords[1]); 
                dout.writeInt(statusCode);
                dout.writeInt(data);                        
                dout.writeUTF(fileName);
                len = 0;
                // send file to client
                for(int i = data; i > 0; i--){              
                  len = fin.read(buffer);        
                  out.write(buffer,0,len);       
                }
                fin.close();
                out.flush();
        	  }else {
        		file = new File(requestWords[1]);
        		if (file.isFile()) {
        		// get file name from file path
                FileInputStream fin = new FileInputStream(requestWords[1]);
                String [] parseFileName = requestWords[1].split("\\\\");
                String fileName = parseFileName[parseFileName.length-1];
                while((len = fin.read(buffer))>0){  // calculate file size
                  data++;                        
                }
                fin.close();
                fin = new FileInputStream(requestWords[1]); 
                dout.writeInt(statusCode);
                dout.writeInt(data);                        
                dout.writeUTF(fileName);
                len = 0;
                // send file to client
                for(int i = data; i > 0; i--){              
                  len = fin.read(buffer);        
                  out.write(buffer,0,len);       
                }
                fin.close();
                out.flush();
        		}
        		else {  // error response about "Wrong file path" request
                  statusCode = -1;
                  dout.writeInt(statusCode);
                  dout.writeInt(errorResponse.length());
                  dout.writeUTF(errorResponse);
                  out.flush();
            	}
        	  }
        	}
          } 
          /* responses about PUT request
           * response return values are "whether the file transfer is okay" response value
           */
          else if("PUT".equals(requestWords[0])) {
        	OutputStream out = clientSocket.getOutputStream();               
          	DataOutputStream dout = new DataOutputStream(out);
            int statusCode = 1;
          	if (requestWords.length == 1) {  // error response "PUT" request
              statusCode = -1;
          	  dout.writeInt(statusCode);
              dout.writeUTF(errorWrongcmd);
              out.flush();
        	}
        	else {  // get file into server
        	  File file = new File(requestWords[1]);
        	  int len, data;
        	  String filename;
        	  byte[] buffer = new byte[1024];                                   
              InputStream in1 = clientSocket.getInputStream();                       
              DataInputStream din = new DataInputStream(in1); 
              data = din.readInt();
              if (data == -1) {
            	statusCode = -1;
                dout.writeInt(statusCode);
                dout.writeUTF("No such file exist");
                out.flush();	  
              }
              else {
                filename = din.readUTF();
                String currentPath = System.getProperty("user.dir");
                FileOutputStream fout = new FileOutputStream(filename);
                // get file from client
                for(int i = data; i > 0; i--){            
                  len = in1.read(buffer);
                  fout.write(buffer,0,len);
                }
                dout.writeInt(statusCode);
                dout.writeUTF(filename + " transferred.    " + data + " kbytes.");
                fout.flush();
                fout.close();
                out.flush();  	
        	  }
        	}
          }
          else {  // error response about "Wrong cmd"
        	OutputStream out = clientSocket.getOutputStream();               
          	DataOutputStream dout = new DataOutputStream(out);
            dout.writeUTF(errorWrongcmd);
            out.flush();
          }
        }
      } 
    }  
    catch( Exception e ){
      e.printStackTrace();
    }
  }
}