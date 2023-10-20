package resources;
import database.UserDao;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.FormParam;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import model.User;

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
        // Check if the user exists
        User user = UserDao.instance.selectUser(username);
        if (user != null) {
            // Here you should use secure methods such as hashing for password comparison
            return user.getPassword().equals(password);
        }
        return false;
    }
}
