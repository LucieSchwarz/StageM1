import java.util.ArrayList;

import com.jme3.app.SimpleApplication;
import com.jme3.material.Material;
import com.jme3.material.RenderState.BlendMode;
import com.jme3.scene.Geometry;
import com.jme3.scene.shape.Box;
import com.jme3.renderer.queue.RenderQueue.Bucket;

import java.io.*;
	
public class Cube extends SimpleApplication {
	    
	public static void main (String [] args) throws IOException{
		Cube app = new Cube();
		app.start();
	}
	
	
	    
    @Override
    public void simpleInitApp(){

    	//Lancement du script python
    	
    	Runtime runtime = Runtime.getRuntime();
    	try {;
    		String[] args1 = { "cmd.exe", "/C", "cd C:/Users/Lucie/Documents/M1_S2/Stage/ && python final.py ima1.jpg ima3.jpg" };
    		//String[] args1 = { "cmd.exe", "/C", "cd C:/Users/Lucie/Documents/M1_S2/Stage/ && python recupRect.py" };

			final Process process1 = runtime.exec(args1);
			process1.waitFor();
			System.out.println("SUCCES");
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("ECHEC");
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	
    	
    	//Recuperation des dimension du Cube depuis un fichier txt
    	
    	ArrayList<Integer> valeurs = new ArrayList<Integer>();
		
		try{
			InputStream ips=new FileInputStream("C:/Users/Lucie/Documents/M1_S2/Stage/leNomDuFichier.txt");					InputStreamReader ipsr=new InputStreamReader(ips);
			BufferedReader br=new BufferedReader(ipsr);
			String ligne;
			while ((ligne=br.readLine())!=null){
				System.out.println(ligne);
				valeurs.add(Integer.parseInt(ligne));
			}
			br.close(); 
		}		
		catch (Exception e){
			System.out.println(e.toString());
		}		
		
		int h = valeurs.remove(0);
		int w = valeurs.remove(0);
		int p = valeurs.remove(0);
		
		System.out.println(h+" "+w+" "+p);

		
		//Construction du cube
		
        Box b = new Box(w, h, p);
        Geometry geom = new Geometry("Box", b);
        
        Material mat1 = new Material(assetManager, "Common/MatDefs/Misc/ShowNormals.j3md");

        mat1.getAdditionalRenderState().setBlendMode(BlendMode.Alpha);

        geom.setQueueBucket(Bucket.Transparent);

        geom.setMaterial(mat1);
	    rootNode.attachChild(geom);
    }
	    
	

}
