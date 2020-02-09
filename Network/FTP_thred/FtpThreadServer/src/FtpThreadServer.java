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
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Properties;

class returnClass{
	 int status = 1;
	 String value;
}

class returnClass1{
	int status = 1;
	int dataSize= 0;
	String fileName = "";
	String path = "";
}

public class FtpThreadServer {
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
  // CD response method return status, CD response value
  public returnClass moveWorkDictionary(String[] requestWords, String errorResponse) throws IOException {
	FtpThreadServer serve = new FtpThreadServer();
	returnClass result = new returnClass();
	String curPath=""; 
  	if(requestWords.length == 2) {   // response about "CD" request
  	  if("NoPath".equals(requestWords[1])) {
  		result.value = System.getProperty("user.dir");
  	  }else {
  		result.value = requestWords[1];
  	  }
  	  return result;
  	}
    else {  // response about "CD path" request
      if ("NoPath".equals(requestWords[2])) {
    	curPath = new java.io.File(requestWords[1]).getCanonicalPath();  
      }
      else {
    	File f = new File(requestWords[2]+"/"+requestWords[1]);
    	curPath = f.getCanonicalPath();
      }
      File dir = new File(curPath); 
      if (dir.isDirectory()) { // response about "CD relative path"
        result.value = curPath;
    	return result;
      }
      else {  // response about "CD absolute path"
        dir = new File(requestWords[1]);  
    	if (dir.isDirectory()) {
          result.value = requestWords[1];
    	  return result;
    	}
    	else {  // error response about "Wrong path"
          result.status = -1; 
    	  result.value = errorResponse;
    	  return result;
    	}
      } 
	}
  }
  // LIST response method return status, LIST response value
  public returnClass showList(String[] requestWords, String errorResponse )  throws IOException{
	  FtpThreadServer serve = new FtpThreadServer();
	  returnClass result = new returnClass();
	  String curPath = "";
  	  // response about "LIST .", "LIST" request
      if (requestWords.length == 2){  
    	if("NoPath".equals(requestWords[1])) {
    	  File dir = new File(System.getProperty("user.dir"));
    	  result.value = serve.findLISTandResponse(dir);
    	}else {
    	  File dir = new File(requestWords[1]);
    	  result.value = serve.findLISTandResponse(dir);
    	}
  	    return result;
      }
  	  // response about "LIST relative path" and "LIST absolute path" request
  	  else {
  		if ("NoPath".equals(requestWords[2])) {
  	      curPath = new java.io.File(requestWords[1]).getCanonicalPath();  
  	    }
  	    else {
  	      File f = new File(requestWords[2]+"/"+requestWords[1]);
  	      curPath = f.getCanonicalPath();
  	    }  
  		File dir = new File(curPath);
  	    if (dir.isDirectory()) { // about relative path
  		  result.value = serve.findLISTandResponse(dir);
  		  return result;
  	    }
  	    else { // about absolute path
  	      File dir1 = new File(requestWords[1]);
          if (dir1.isDirectory()) {
            result.value = serve.findLISTandResponse(dir1);
            return result;
          }
          else {  //error response about "Wrong path" 
            result.status = -1;
        	result.value = errorResponse;
        	return result;
          }			  
  	    }
  	  }
  }
  // GET response method return status, file size, file name, path 
  public returnClass1 getfile(String[] requestWords, String errorResponse, String errorWrongcmd) throws IOException {
    FtpThreadServer serve = new FtpThreadServer();
	returnClass1 result = new returnClass1();
    String currentPath = "";
    // error response about "Wrong cmd"
  	if (requestWords.length == 2) {   
      result.status = -1;
      result.fileName = errorWrongcmd;
  	  return result;
  	}
    // find file and response file about "GET file name" or "GET file path" request
  	else {
  	  if("NoPath".equals(requestWords[2])){
  		currentPath = System.getProperty("user.dir");	  
  	  }else {
  		currentPath = requestWords[2];
  	  }
  	  byte[] buffer = new byte[1024];   
      int len;                                
      File file = new File(currentPath + "\\" +requestWords[1]);
  	  if (file.isFile()) {
  		result.path = file.getCanonicalPath();
  	    FileInputStream fin = new FileInputStream(result.path);
  	    String [] parseFileName = requestWords[1].split("\\\\|/");
        result.fileName = parseFileName[parseFileName.length-1];
        System.out.println(result.fileName);
        while((len = fin.read(buffer))>0){  // calculate file size
          result.dataSize++;                        
        }
        fin.close();    
        return result;
  	  }else {
  		  file = new File(requestWords[1]);
  		  if (file.isFile()) {
  		  // get file name from file path
  			result.path = requestWords[1];
            FileInputStream fin = new FileInputStream(requestWords[1]);
            String [] parseFileName = requestWords[1].split("\\\\|/");
            result.fileName = parseFileName[parseFileName.length-1];
            while((len = fin.read(buffer))>0){  // calculate file size
              result.dataSize++;                        
            }
            fin.close();
            result.status = 2;
            return result;
  		  }
  		  else {  // error response about "Wrong file path" request
            result.status = -1;
            result.fileName = errorResponse;
            return result;
  		  }
  	    }
  	  }  
  }
  // put response method return status, put response value
  public returnClass putFile(Socket client, String [] requestWords,  String errorWrongcmd) throws IOException {
	returnClass result = new returnClass();
    if (requestWords.length == 2) {  // error response "PUT" request
      result.status = -1;
      result.value = errorWrongcmd;
      return result;
    }
    else {  // get file into server
  	  File file = new File(requestWords[1]);
  	  synchronized(requestWords[1].intern()) {
  	    int len, data;
  	    String filename;
  	    byte[] buffer = new byte[1024];                                   
        InputStream in = client.getInputStream();                       
        DataInputStream din = new DataInputStream(in); 
        data = din.readInt();
        if (data == -1) {
          result.status = -1;
          result.value = "No such file exist";
          return result;	  
        }
        else {
    	  System.out.println(client.getPort());  
      	  filename = din.readUTF();
          FileOutputStream fout = new FileOutputStream(filename);
          // get file from client
          for(int i = data; i > 0; i--){            
            len = in.read(buffer);
            fout.write(buffer,0,len);
          }
          result.value = filename + " transferred.    " + data + " kbytes.";
          fout.flush();
          fout.close();
          return result;
        }
      }
  	}    
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
        String errorResponse = "Failed directory name is invalid.";
        String errorWrongcmd = "Wrong cmd try again.";
        System.out.println("Accepted connection from" + clientSocket);
        new Thread(new Runnable() {
          public void run() {    
            try {
        	  FtpThreadServer serve = new FtpThreadServer();
        	  String response, request;
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
        	      returnClass result = new returnClass();
        	      OutputStream out = clientSocket.getOutputStream();               
        	      DataOutputStream dout = new DataOutputStream(out);
        	      result = serve.moveWorkDictionary(requestWords, errorResponse);
        	      dout.writeInt(result.status);
        	      dout.writeInt(result.value.length());
        	      dout.writeUTF(result.value);
        	      out.flush();
        	    }
        	    /* responses about LIST request
        	     * response return values are status code, response length, response value
        	    */
        	    else if("LIST".equals(requestWords[0])) {
        	      returnClass result = new returnClass();
        	      OutputStream out = clientSocket.getOutputStream();               
        	      DataOutputStream dout = new DataOutputStream(out);
        	      result = serve.showList(requestWords, errorResponse);
        	      dout.writeInt(result.status);
        	      dout.writeInt(result.value.length());
        	      dout.writeUTF(result.value);
        	      out.flush();
        	    }
        	    /* responses about GET request
        	     * response return values are status code, file size, file name, file response value
        	    */
        	    else if("GET".equals(requestWords[0])) {   
        	      byte[] buffer = new byte[1024];  
        	      returnClass1 result = new returnClass1();
        	      OutputStream out = clientSocket.getOutputStream();               
        	      DataOutputStream dout = new DataOutputStream(out);
        	      result = serve.getfile(requestWords, errorResponse, errorWrongcmd);
        	      dout.writeInt(result.status);
        	      dout.writeInt(result.dataSize);
        	      dout.writeUTF(result.fileName);
        	      if (result.status != -1) {
        	        int len = 0;
        	        // send file to client
        	        FileInputStream fin = new FileInputStream(result.path);   
        	        for(int i = result.dataSize; i > 0; i--){              
          	          len = fin.read(buffer);        
          	          out.write(buffer,0,len);       
          	        }
          	        fin.close();
        	        out.flush();
        	      }
        	    } 
        	    /* responses about PUT request
                 * response return values are "whether the file transfer is okay" response value
                 */
        	    else if("PUT".equals(requestWords[0])) {
        	      OutputStream out = clientSocket.getOutputStream();               
        	      DataOutputStream dout = new DataOutputStream(out);
        	      returnClass result = new returnClass();
        	      
        	      result = serve.putFile(clientSocket, requestWords, errorWrongcmd);
        	      dout.writeInt(result.status);
        	      dout.writeUTF(result.value);
        	      out.flush();
        	    }
        	    else {  // error response about "Wrong cmd"
        	      OutputStream out = clientSocket.getOutputStream();               
        	      DataOutputStream dout = new DataOutputStream(out);
        	      dout.writeUTF(errorWrongcmd);
        	      out.flush();
        	    }
        	  } 
            }catch (IOException e) {
        	  e.printStackTrace();
        	  try {clientSocket.close();} catch (IOException ex) { }
        	}  
          }
        }).start();
      }
	}
    catch( Exception e1 ){
      e1.printStackTrace();
    }
  }
}