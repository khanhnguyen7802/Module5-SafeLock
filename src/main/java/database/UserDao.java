package database;

import model.User;

import java.util.HashMap;
import java.util.Map;

public enum UserDao {
    instance;
    private Map<String, User> userMap;

    private UserDao() {
        User user1 = new User("Samthing","ppap1234");
        userMap.put("Samthing",user1);
        User user2 = new User("shunshun","ppap1234");
        userMap.put("shunshun",user1);
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