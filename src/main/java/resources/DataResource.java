package resources;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

// Define an endpoint to receive data
@Path("/data")
public class DataResource {
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response postData(String data) {
        System.out.println("Received data: " + data);
        // Process the data here
        return Response.status(200).entity("Data received successfully").build();
    }
}

///Not working properly