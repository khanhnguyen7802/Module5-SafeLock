package database;

import model.User;

import java.util.HashMap;
import java.util.Map;

public enum UserDao {
    instance;
    private Map<String, User> userMap;

    private UserDao() {
        this.userMap = new HashMap<>();
    }

    public void insertUser(User user) {
        userMap.put(user.getName(), user);
    }

    public User selectUser(String username) {
        return userMap.get(username);
    }

    public Map<String, User> getUserMap() {
        return userMap;
    }
}
