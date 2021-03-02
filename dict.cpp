#include <unordered_map>
#include <string>

#define Dict std::unordered_map<std::string, std::string>

extern "C" Dict* make_dict() {
    Dict *dict = new Dict();

    return dict;
}


extern "C" void set_value(Dict* dict, char* key, char* value) {
    std::string* key_string = new std::string(key);
    std::string* value_string = new std::string(value);
    (*dict)[*key_string] = *value_string;
}


extern "C" const char* get_value(Dict* dict, char* key) {
    std::string s(key);

    return (*dict)[s].c_str();
}
