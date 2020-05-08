#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#
from typing import List
# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for _ in range(n)]
        stack = []
        preTime = 0
        for log in logs:
            items = log.split(':')
            idx = int(items[0])
            typeName = items[1]
            ts = int(items[2])
            if stack:
                res[stack[-1]] += ts - preTime
            preTime = ts
            if typeName=='start':
                stack.append(idx)
            else:
                last = stack.pop()
                res[last] += 1
                preTime +=1
            # print(stack)
            # print(preTime)
            # print(res)
        return res

# @lc code=end

n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

n = 79
logs = ["0:start:0","1:start:2","2:start:5","3:start:7","4:start:8","5:start:11","6:start:12","7:start:17","8:start:20","9:start:24","10:start:29","11:start:34","12:start:36","13:start:38","14:start:42","15:start:46","16:start:47","17:start:50","18:start:54","19:start:59","20:start:61","21:start:63","22:start:64","23:start:67","24:start:71","25:start:74","26:start:78","27:start:79","28:start:80","29:start:84","30:start:86","31:start:88","32:start:92","33:start:93","34:start:96","35:start:98","36:start:101","37:start:104","38:start:108","39:start:111","40:start:115","41:start:119","42:start:122","43:start:124","44:start:129","45:start:133","46:start:135","47:start:139","48:start:140","49:start:141","50:start:146","51:start:148","52:start:152","53:start:154","54:start:155","55:start:157","56:start:159","57:start:162","58:start:163","59:start:164","60:start:166","61:start:167","62:start:171","63:start:175","64:start:180","65:start:185","66:start:187","67:start:192","68:start:193","69:start:195","70:start:200","71:start:205","72:start:208","73:start:211","74:start:213","75:start:214","76:start:219","77:start:221","78:start:224","47:start:233","28:start:234","10:start:239","10:end:240","28:end:243","47:end:245","49:start:246","49:end:247","78:end:248","40:start:253","64:start:256","64:end:259","38:start:260","38:end:265","36:start:268","36:end:269","40:end:274","31:start:277","46:start:281","46:end:286","31:end:288","77:end:289","28:start:293","28:end:294","76:end:295","14:start:299","14:end:302","75:end:305","74:end:309","4:start:313","4:end:316","73:end:317","72:end:322","42:start:324","42:end:329","71:end:331","70:end:335","69:end:340","68:end:343","67:end:346","21:start:347","61:start:349","61:end:354","21:end:359","15:start:361","56:start:362","56:end:365","15:end:366","66:end:370","65:end:374","64:end:379","63:end:383","72:start:385","5:start:386","55:start:388","55:end:392","5:end:393","72:end:395","3:start:397","50:start:398","50:end:402","22:start:403","22:end:406","3:end:407","62:end:408","70:start:413","76:start:417","76:end:421","70:end:422","61:start:424","61:end:427","61:end:429","73:start:433","73:end:437","70:start:440","70:end:443","60:end:447","59:end:448","58:end:449","57:end:453","56:end:458","55:end:460","54:end:465","22:start:467","65:start:470","65:end:473","22:end:476","53:end:481","9:start:484","9:end:485","52:end:489","51:end:491","50:end:495","38:start:497","38:end:500","49:end:505","48:end:507","40:start:511","40:end:514","35:start:518","35:end:519","47:end:520","46:end:524","45:end:526","44:end:531","69:start:536","69:end:541","43:end:544","42:end:546","41:end:551","40:end:552","39:end:557","71:start:559","71:end:562","38:end:563","77:start:565","77:end:566","30:start:567","30:end:569","37:end:574","52:start:575","52:end:578","36:end:583","56:start:587","56:end:589","35:end:593","34:end:598","33:end:603","32:end:604","59:start:607","59:end:611","31:end:616","42:start:618","42:end:622","39:start:626","39:end:629","8:start:630","8:end:633","30:end:635","67:start:638","67:end:643","29:end:646","8:start:647","8:end:651","28:end:654","36:start:656","36:end:657","27:end:660","26:end:663","25:end:668","24:end:670","23:end:672","22:end:676","21:end:681","20:end:685","19:end:689","18:end:694","17:end:695","16:end:697","15:end:700","66:start:702","66:end:704","14:end:706","28:start:708","44:start:711","44:end:716","28:end:719","13:end:720","12:end:722","11:end:724","21:start:728","39:start:730","39:end:735","21:end:740","10:end:745","9:end:749","42:start:752","42:end:753","33:start:757","33:end:760","70:start:765","70:end:767","27:start:771","27:end:775","18:start:780","35:start:785","35:end:789","18:end:792","13:start:797","13:end:800","8:end:803","7:end:806","63:start:808","5:start:809","5:end:811","63:end:815","6:end:816","5:end:819","4:end:821","22:start:822","22:end:824","3:end:828","77:start:832","10:start:835","10:end:837","77:end:840","36:start:841","71:start:844","71:end:845","36:end:846","2:end:851","1:end:852","38:start:854","38:end:857","49:start:862","49:end:863","0:end:867"]

res = Solution().exclusiveTime(n, logs)
print(res)