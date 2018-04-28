/*
 * the previously crawled data are not fully separated or parsed.
 * this file separates the file in the desired format
 * 
 * 
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Format {

	public static void main(String[] args) throws InterruptedException, IOException {
		// TODO Auto-generated method stub
		File f;
		 String fn;
		 //create output file
		 File file = new File("12-8TWTR.txt");
			file.createNewFile();
			PrintWriter writer = new PrintWriter(file); 
			//read input file
		f= new File("12-8 (4).txt");
			Scanner in= new Scanner(f);
			 String nl=System.getProperty("line.separator");
			//arraylists to hold values before writing to the file
			ArrayList price = new ArrayList<String>();
	         ArrayList time = new ArrayList<String>();
	         ArrayList open = new ArrayList<String>();
	         ArrayList close = new ArrayList<String>();
	         ArrayList volume = new ArrayList<String>();
	         ArrayList AvgVolume = new ArrayList<String>();
	         ArrayList Bid = new ArrayList<String>();
	         ArrayList change = new ArrayList<String>();
	         ArrayList changePerc = new ArrayList<String>();
	         ArrayList ask = new ArrayList<String>();
	         ArrayList marketCap = new ArrayList<String>();
	         ArrayList beta = new ArrayList<String>();
	         ArrayList PEratio = new ArrayList<String>();
	         ArrayList eps = new ArrayList<String>();
			

				String temp=null;
				String temp2=null;
				String t=null;
				int kk=0;
				int counter=0;
				//until you reach the end of file read the file line by line.
				while(in.hasNextLine()) {
					//split the line
					 String[] splitStr=t.split("\\s+");
					System.out.println(" size-"+splitStr.length+" "+counter);
					counter++;
					price.add(splitStr[0]);
					if(splitStr[2].equals("Dec")) {
						temp="12";
					}
//					if(splitStr[2].equals("Nov")) {
//						temp="11";
//					}
					
					//extract and store required attributes
					String date="2017-"+temp+"-"+splitStr[3]+" "+splitStr[4];
					
					time.add(date);
					change.add(splitStr[13]);
					changePerc.add(splitStr[14]);
					close.add(splitStr[17]);
					open.add(splitStr[19]);
					temp=splitStr[21]+splitStr[22]+splitStr[23];
					Bid.add(temp);
					temp=splitStr[25]+splitStr[26]+splitStr[27];
					ask.add(temp);
					volume.add(splitStr[34]);
					AvgVolume.add(splitStr[37]);
					marketCap.add(splitStr[40]);
					beta.add(splitStr[42]);
					PEratio.add(splitStr[46]);
					eps.add(splitStr[49]);
					
					
					
					
				//Thread.sleep(1000);
			         
				}
				// write the output to the file
				writer.write("price"+"\t"+"time"+"\t"+"change"+"\t"+
							"changePerc"+"\t"+"close"+"\t"+"oepn"+"\t"+
						"volume"+"\t"+"avgVolume"+"\t"+"bid"+"\t"+"ask"+"\t"+
							"MarketCapp"+"\t"+"PERatio"+"\t"+"beta"+"\t"+"eps");
				writer.write((nl));			
				
				for(int i=0;i<price.size();i++) {
					writer.write(price.get(i)+"\t"+
							time.get(i)+"\t"+
							change.get(i)+"\t"+
							changePerc.get(i)+"\t"+
							close.get(i)+"\t"+
							open.get(i)+"\t"+
							volume.get(i)+"\t"+
							AvgVolume.get(i)+"\t"+
							Bid.get(i)+"\t"+
							ask.get(i)+"\t"+
							marketCap.get(i)+"\t"+
							PEratio.get(i)+"\t"+
							beta.get(i)+"\t"+
							eps.get(i));
					writer.write((nl));
					
					
				}
				writer.close(); //close the output file
				
				
	}

}