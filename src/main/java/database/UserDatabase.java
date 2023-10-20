package database;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import model.User;
public class UserDatabase {
        private final String jdbcURL = "jdbc:mysql://localhost:3306/db_name";///change it to exact url
        private final String jdbcUsername = "username";
        private final String jdbcPassword = "password";

        private static final String INSERT_USERS_SQL = "INSERT INTO users" + "  (username, password) VALUES " +
                " (?, ?);";
        private static final String SELECT_USER_BY_USERNAME = "select id,username,password from users where username =?";

        public UserDatabase() {
        }

        protected Connection getConnection() {
            Connection connection = null;
            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                connection = DriverManager.getConnection(jdbcURL, jdbcUsername, jdbcPassword);
            } catch (SQLException | ClassNotFoundException e) {
                e.printStackTrace();
            }
            return connection;
        }

        public void insertUser(User user) throws SQLException {
            try (Connection connection = getConnection();
                 PreparedStatement preparedStatement = connection.prepareStatement(INSERT_USERS_SQL)) {
                preparedStatement.setString(1, user.getName());
                preparedStatement.setString(2, user.getPassword());
                preparedStatement.executeUpdate();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

        public User selectUser(String username) {
            User user = null;
            try (Connection connection = getConnection();
                 PreparedStatement preparedStatement = connection.prepareStatement(SELECT_USER_BY_USERNAME)) {
                preparedStatement.setString(1, username);
                ResultSet rs = preparedStatement.executeQuery();

                while (rs.next()) {
                    int id = rs.getInt("id");
                    String name = rs.getString("username");
                    String password = rs.getString("password");
                    user = new User();
                    user.setId(id);
                    user.setName(name);
                    user.setPassword(password);
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
            return user;
        }
    }
