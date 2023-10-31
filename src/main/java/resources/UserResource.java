package resources;

import database.UserDatabase;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import model.User;

@Path("/user")
public class UserResource {
    private static final String USERNAME = "username";
    private static final String PASSWORD = "password";
    private static final String GPS = "gps";

    @POST
    @Path("/signup")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public Response signup(@FormParam(USERNAME) String username, @FormParam(PASSWORD) String password) {
        User user = new User(username, password);
        UserDatabase.insertUser(user);
        return Response.ok("Signup successful").build();
    }

    @POST
    @Path("/login")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public Response login(@FormParam(USERNAME) String username, @FormParam(PASSWORD) String password) {
        if (isValidUser(username, password)) {
            return Response.ok("Login Successful").build();
        } else {
            return Response.status(Response.Status.UNAUTHORIZED).build();
        }
    }

    private boolean isValidUser(String username, String password) {
        User user = UserDatabase.selectUser(username);
        return user != null && user.getPassword().equals(password);
    }
    @GET
    @Path("/gps")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public Response getGPS(@FormParam(USERNAME) String username) {
        String gps = UserDatabase.getGPS(username);
        if (gps != null) {
            return Response.ok(gps).build();
        } else {
            return Response.status(Response.Status.NOT_FOUND).entity("GPS not found for the user").build();
        }
    }
}
