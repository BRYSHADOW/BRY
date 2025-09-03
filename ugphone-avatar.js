// UgPhone Avatar Menu by BRY

(function(){
    'use strict';

    let localData = null;

    function addAvatar(){
        let btn=document.createElement("img");
        btn.src="https://cdn3.notevn.com/D5snYkyOwP.png";
        btn.style.cssText=`
            position:fixed;bottom:20px;right:20px;
            width:70px;height:70px;border-radius:50%;
            cursor:pointer;z-index:999999;box-shadow:0 4px 12px rgba(0,0,0,.3);
        `;
        btn.onclick=toggleMenu;
        document.body.appendChild(btn);
    }

    function createMenu(){
        let menu=document.createElement("div");
        menu.id="ug-menu";
        menu.style.cssText=`
            position:fixed;bottom:100px;right:20px;
            display:none;flex-direction:column;gap:10px;
            background:#fff;padding:12px;border-radius:12px;
            box-shadow:0 4px 10px rgba(0,0,0,.3);z-index:100000;
        `;
        document.body.appendChild(menu);

        let btn1=document.createElement("button");
        btn1.innerText="🔑 Nhập Local";
        btn1.onclick=enterLocal;
        menu.appendChild(btn1);

        let btn2=document.createElement("button");
        btn2.innerText="🎁 Lấy Trial Free";
        btn2.onclick=claimTrial;
        menu.appendChild(btn2);
    }

    function toggleMenu(){
        let menu=document.getElementById("ug-menu");
        if(!menu)return;
        menu.style.display=(menu.style.display==="flex")?"none":"flex";
    }

    function enterLocal(){
        let input=prompt("Dán JSON local của bạn:");
        if(!input)return;
        try{
            localData=JSON.parse(input);
            alert("✅ Đã lưu local!");
        }catch(e){alert("❌ Sai JSON!");}
    }

    async function claimTrial(){
        if(!localData||!localData["UGPHONE-Token"]){
            alert("❌ Chưa nhập local!");
            return;
        }
        let token=localData["UGPHONE-Token"];
        try{
            let res=await fetch("https://api.ugphone.com/device/freeTrial",{
                method:"POST",
                headers:{
                    "Content-Type":"application/json",
                    "Authorization":"Bearer "+token
                },
                body:"{}"
            });
            let data=await res.json();
            console.log("Trial:",data);
            if(data.success){
                alert("🎉 Nhận máy free thành công!");
            }else{
                alert("⚠️ Thất bại: "+(data.message||JSON.stringify(data)));
            }
        }catch(e){alert("❌ Lỗi: "+e.message);}
    }

    window.addEventListener("load",()=>{setTimeout(()=>{addAvatar();createMenu();},2000);});
})();