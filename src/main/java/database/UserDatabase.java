package database;

import model.User;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class UserDatabase {
    private static final String DB_URL = "jdbc:postgresql://localhost:5432/project";
    private static final String USER = "postgres";
    private static final String PASSWORD = "Sairen1360!";

    public static Connection connect() throws SQLException {
        return DriverManager.getConnection(DB_URL, USER, PASSWORD);
    }

    public static void insertUser(User user) {
        try (Connection connection = connect()) {
            String query = "INSERT INTO users (username, password) VALUES (?, ?)";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, user.getName());
            statement.setString(2, user.getPassword());
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static User selectUser(String username) {
        User user = null;
        try (Connection connection = connect()) {
            String query = "SELECT * FROM users WHERE username = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, username);
            ResultSet resultSet = statement.executeQuery();

            if (resultSet.next()) {
                String name = resultSet.getString("username");
                String password = resultSet.getString("password");
                user = new User(name, password);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return user;
    }
}
