import database.UserDatabase;
import org.junit.jupiter.api.Test;

import java.sql.SQLException;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestUpdate {
    String username = "testuser";
    String gps = "TestGPS";
    @Test
    public void testUpdateGPS() {

    // Invoke the updateGPS method
        UserDatabase.updateGPS(username, gps);

    // Check if the update was successful
        String updatedGPS = UserDatabase.getGPS(username);
        assertEquals(gps, updatedGPS);
    }

    @Test
    public void testUpdatePassword() {
        String username = "testuser";
        String newPassword = "newPassword123";

        // Invoke the updatePassword method
        UserDatabase.updatePassword(username, newPassword);

        // Check if the update was successful
        // You can add your own implementation here to verify the update
    }
}
