loadstring(game:HttpGet(("https://raw.githubusercontent.com/daucobonhi/Ui-Redz-V2/refs/heads/main/UiREDzV2.lua")))()

       local Window = MakeWindow({
         Hub = {
         Title = "BRY V2",
         Animation = "FB: Chau Mcbr"
         },
        Key = {
        KeySystem = false,
        Title = "Key System",
        Description = "",
        KeyLink = "",
        Keys = {"1234"},
        Notifi = {githubusercontent
        Notifications = true,
        CorrectKey = "Running the Script...",
       Incorrectkey = "The key is incorrect",
       CopyKeyLink = "Copied to Clipboard"
      }
    }
  })

       MinimizeButton({
       Image = "http://www.roblox.com/asset/?id=96114075322069",
       Size = {40, 40},
       Color = Color3.fromRGB(10, 10, 10),
       Corner = true,
       Stroke = false,
       StrokeColor = Color3.fromRGB(255, 0, 0)
      })
      
------ Tab
     local Tab1o = MakeTab({Name = "Menu 1"})
     local Tab2o = MakeTab({Name = "Menu 2"})
------- BUTTON
    
    AddButton(Tab1o, {
     Name = "Redz Hub",
    Callback = function()
	  local Settings = {
  JoinTeam = "Pirates"; -- Pirates/Marines
  Translator = true; -- true/false
}

loadstring(game:HttpGet("https://raw.githubusercontent.com/realredz/BloxFruits/refs/heads/main/Source.lua"))(Settings)
  end
  })
  AddButton(Tab2o, {
     Name = "lumtraitudoisv",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/marisdeptrai/Script-Free/main/FruitFinder.lua"))()
  end
  })
  AddButton(Tab1o, {
     Name = "Volcano Hub",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/wpisstestfprg/Volcano/refs/heads/main/VolcanoLocal.lua", true))()
  end
  })
  AddButton(Tab2o, {
     Name = "hack dieu chinh",
    Callback = function()
	  loadstring(Game:HttpGet("https://raw.githubusercontent.com/VanThanhIOS/OniiChanVanThanhIOS/refs/heads/main/oniichanpakavanthanhios"))()
  end
  })
  AddButton(Tab1o, {
     Name = "Script Trẩu",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/LuaCrack/TrauHub/refs/heads/main/TrauXt"))()
  end
  })
  AddButton(Tab1o, {
     Name = "Rubu RedZ Hub",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/LuaCrack/RubuRoblox/refs/heads/main/RubuBF"))()
  end
  })
  AddButton(Tab1o, {
     Name = "ASTRAL Hub",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/Overgustx2/Main/refs/heads/main/BloxFruits_25.html"))()
  end
  })
  AddButton(Tab1o, {
     Name = "W-AZURE mới",
    Callback = function()
	  getgenv().Team = "Pirates"
getgenv().AutoLoad = false --Will Load Script On Server Hop
getgenv().SlowLoadUi = false
getgenv().ForceUseSilentAimDashModifier = false --Force turn on silent aim , if error then executor problem
getgenv().ForceUseWalkSpeedModifier = false --Force turn on Walk Speed Modifier , if error then executor problem
loadstring(game:HttpGet("https://api.luarmor.net/files/v3/loaders/3b2169cf53bc6104dabe8e19562e5cc2.lua"))()
  end
  })
  AddButton(Tab2o, {
     Name = "Treo Farmlv",
    Callback = function()
	  getgenv().simple_settings = {

    ["MASTERY"] = { -- Settings related to leveling up weapon or skill mastery

        ["ACTIVE"] = true, -- Enable or disable mastery leveling (true = enabled, false = disabled)

        ["METHOD"] = "Half", -- Method for gaining mastery, "Half"[300] or "Full"[600]

    },

 

    ["OBJECTIVE"] = { -- Goals for farming and unlocking features

        ["GODHUMAN"] = true, -- Automatically unlock the "Godhuman" fighting style

        ["RACE-V3"] = true, -- Automatically upgrade character race to V3 if possible Human, Mink, (Fishman, Ghoul, Cyborg) soon

        ["FRAGMENT"] = 100000, -- Limit number of fragments to collect

 

        -- SWORD

        ["CANVANDER"] = true,

        ["BUDDY-SWORD"] = true,

        ["CURSED-DUAL-KATANA"] = true,

        ["SHARK-ANCHOR"] = true, -- soon..

 

        --GUN

        ["ACIDUM-RIFLE"] = true,

        ["VENOM-BOW"] = true,

        ["SOUL-GUITAR"] = true,

    },

 

    ["FRUITPURCHASE"] = true, -- Automatically purchase fruits based on priority list

    ["PRIORITYFRUIT"] = { -- List of preferred fruits to purchase or eat in order of priority

        [1] = "Dragon-Dragon",

        [2] = "Flame-Flame",

        [3] = "Rumble-Rumble",

        [4] = "Human-Human: Buddha",

        [5] = "Dark-Dark",

    },

 

    ["FPSCAP"] = 30, -- Limit the frame rate to optimize performance

    ["LOWTEXTURE"] = true -- Reduce graphic quality for better performance

}

loadstring(game:HttpGet("https://raw.githubusercontent.com/simple-hubs/contents/refs/heads/main/bloxfruit-kaitan-main.lua"))()
  end
  })
AddButton(Tab1o, {
     Name = "Script Min Siêu Vip",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/LuaCrack/Min/refs/heads/main/MinXoV"))()
  end
  })
