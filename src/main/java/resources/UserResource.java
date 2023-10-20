package resources;

import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.FormParam;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/login")
public class UserResource {

    private static final String USERNAME = "username";
    private static final String PASSWORD = "password";

    @POST
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public Response login(@FormParam(USERNAME) String username, @FormParam(PASSWORD) String password) {
        // Here, you can implement your authentication logic
        if (isValidUser(username, password)) {
            return Response.ok("Login Successful").build();
        } else {
            return Response.status(Response.Status.UNAUTHORIZED).build();
        }
    }

    private boolean isValidUser(String username, String password) {
        // Here, you can implement your validation logic, possibly checking against a database or any other data store.
        // For the purpose of this example, we are using a hardcoded username and password.
        return "admin".equals(username) && "admin123".equals(password);
    }
}
